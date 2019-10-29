"""
Offsite Spider Middleware

See documentation in docs/topics/spider-middleware.rst
"""
import re
import logging
import warnings

from scrapy import signals
from scrapy.http import Request
from scrapy.utils.httpobj import urlparse_cached

logger = logging.getLogger(__name__)


class OffsiteMiddleware(object):

    def __init__(self, stats):
        self.stats = stats

    @classmethod
    def from_crawler(cls, crawler):
        o = cls(crawler.stats)
        crawler.signals.connect(o.spider_opened, signal=signals.spider_opened)
        return o

    def process_spider_output(self, response, result, spider):
        for x in result:
            if isinstance(x, Request):
                if x.dont_filter or self.should_follow(x, spider):
                    yield x
                else:
                    domain = urlparse_cached(x).hostname
                    if domain and domain not in self.domains_seen:
                        self.domains_seen.add(domain)
                        logger.debug(
                            "Filtered offsite request to %(domain)r: %(request)s",
                            {'domain': domain, 'request': x}, extra={'spider': spider})
                        self.stats.inc_value('offsite/domains', spider=spider)
                    self.stats.inc_value('offsite/filtered', spider=spider)
            else:
                yield x

    def should_follow(self, request, spider):
        regex = self.host_regex
        # hostname can be None for wrong urls (like javascript links)
        host = urlparse_cached(request).hostname or ''
        return bool(regex.search(host))

    def get_host_regex(self, spider):
        """Override this method to implement a different offsite policy"""
        allowed_domains = getattr(spider, 'allowed_domains', None)
        if not allowed_domains:
            return re.compile('')  # allow all by default
        url_pattern = re.compile("^https?://.*$")
        for domain in allowed_domains:
            if url_pattern.match(domain):
                message = ("allowed_domains accepts only domains, not URLs. "
                           "Ignoring URL entry %s in allowed_domains." % domain)
                warnings.warn(message, URLWarning)
        domains = [re.escape(d) for d in allowed_domains if d is not None]
        regex = r'^(.*\.)?(%s)$' % '|'.join(domains)
        return re.compile(regex)

    def spider_opened(self, spider):
        self.host_regex = self.get_host_regex(spider)
        self.domains_seen = set()


class URLWarning(Warning):
    pass
