import unittest

from testfixtures import LogCapture
from twisted.internet import defer
from twisted.trial.unittest import TestCase as TwistedTestCase
import six

from scrapy.crawler import CrawlerRunner
from scrapy.exceptions import DropItem
from scrapy.http import Request, Response
from scrapy.item import Item, Field
from scrapy.logformatter import LogFormatter
from scrapy.spiders import Spider
from tests.mockserver import MockServer
from tests.spiders import ItemSpider


class CustomItem(Item):

    name = Field()

    def __str__(self):
        return "name: %s" % self['name']


class LoggingContribTest(unittest.TestCase):

    def setUp(self):
        self.formatter = LogFormatter()
        self.spider = Spider('default')

    def test_crawled(self):
        req = Request("http://www.example.com")
        res = Response("http://www.example.com")
        logkws = self.formatter.crawled(req, res, self.spider)
        logline = logkws['msg'] % logkws['args']
        self.assertEqual(logline,
            "Crawled (200) <GET http://www.example.com> (referer: None)")

        req = Request("http://www.example.com", headers={'referer': 'http://example.com'})
        res = Response("http://www.example.com", flags=['cached'])
        logkws = self.formatter.crawled(req, res, self.spider)
        logline = logkws['msg'] % logkws['args']
        self.assertEqual(logline,
            "Crawled (200) <GET http://www.example.com> (referer: http://example.com) ['cached']")

    def test_flags_in_request(self):
        req = Request("http://www.example.com", flags=['test','flag'])
        res = Response("http://www.example.com")
        logkws = self.formatter.crawled(req, res, self.spider)
        logline = logkws['msg'] % logkws['args']
        self.assertEqual(logline,
        "Crawled (200) <GET http://www.example.com> ['test', 'flag'] (referer: None)")

    def test_dropped(self):
        item = {}
        exception = Exception(u"\u2018")
        response = Response("http://www.example.com")
        logkws = self.formatter.dropped(item, exception, response, self.spider)
        logline = logkws['msg'] % logkws['args']
        lines = logline.splitlines()
        assert all(isinstance(x, six.text_type) for x in lines)
        self.assertEqual(lines, [u"Dropped: \u2018", '{}'])

    def test_scraped(self):
        item = CustomItem()
        item['name'] = u'\xa3'
        response = Response("http://www.example.com")
        logkws = self.formatter.scraped(item, response, self.spider)
        logline = logkws['msg'] % logkws['args']
        lines = logline.splitlines()
        assert all(isinstance(x, six.text_type) for x in lines)
        self.assertEqual(lines, [u"Scraped from <200 http://www.example.com>", u'name: \xa3'])


class LogFormatterSubclass(LogFormatter):
    def crawled(self, request, response, spider):
        kwargs = super(LogFormatterSubclass, self).crawled(
        request, response, spider)
        CRAWLEDMSG = (
            u"Crawled (%(status)s) %(request)s (referer: "
            u"%(referer)s)%(flags)s"
        )
        return {
            'level': kwargs['level'],
            'msg': CRAWLEDMSG,
            'args': kwargs['args']
        }


class LogformatterSubclassTest(LoggingContribTest):
    def setUp(self):
        self.formatter = LogFormatterSubclass()
        self.spider = Spider('default')

    def test_flags_in_request(self):
        pass


class SkipMessagesLogFormatter(LogFormatter):
    def crawled(self, *args, **kwargs):
        return None

    def scraped(self, *args, **kwargs):
        return None

    def dropped(self, *args, **kwargs):
        return None


class DropSomeItemsPipeline(object):
    drop = True

    def process_item(self, item, spider):
        if self.drop:
            self.drop = False
            raise DropItem("Ignoring item")
        else:
            self.drop = True

class ShowOrSkipMessagesTestCase(TwistedTestCase):
    def setUp(self):
        self.mockserver = MockServer()
        self.mockserver.__enter__()
        self.base_settings = {
            'LOG_LEVEL': 'DEBUG',
            'ITEM_PIPELINES': {
                __name__ + '.DropSomeItemsPipeline': 300,
            },
        }

    def tearDown(self):
        self.mockserver.__exit__(None, None, None)

    @defer.inlineCallbacks
    def test_show_messages(self):
        crawler = CrawlerRunner(self.base_settings).create_crawler(ItemSpider)
        with LogCapture() as lc:
            yield crawler.crawl(mockserver=self.mockserver)
        self.assertIn("Scraped from <200 http://127.0.0.1:", str(lc))
        self.assertIn("Crawled (200) <GET http://127.0.0.1:", str(lc))
        self.assertIn("Dropped: Ignoring item", str(lc))

    @defer.inlineCallbacks
    def test_skip_messages(self):
        settings = self.base_settings.copy()
        settings['LOG_FORMATTER'] = __name__ + '.SkipMessagesLogFormatter'
        crawler = CrawlerRunner(settings).create_crawler(ItemSpider)
        with LogCapture() as lc:
            yield crawler.crawl(mockserver=self.mockserver)
        self.assertNotIn("Scraped from <200 http://127.0.0.1:", str(lc))
        self.assertNotIn("Crawled (200) <GET http://127.0.0.1:", str(lc))
        self.assertNotIn("Dropped: Ignoring item", str(lc))


if __name__ == "__main__":
    unittest.main()
