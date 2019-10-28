"""
"""
import json
import requests
import urllib
import urllib2
import uuid

from django.conf import settings

logging = settings.LOG


class BaseClient(object):

    def __init__(self, host=None, require_trusted=True, verbose=True):
        
        if not host:
            if settings.CENTRAL_SERVER_URL:
                self.url = settings.CENTRAL_SERVER_URL
            else:
                self.url = "%s://%s/" % (settings.SECURESYNC_PROTOCOL, settings.CENTRAL_SERVER_HOST)
            
            self.parsed_url = urllib2.urlparse.urlparse(self.url)
        
        else:
            self.parsed_url = urllib2.urlparse.urlparse(host)
            self.url = "%s://%s" % (self.parsed_url.scheme, self.parsed_url.netloc)
        
        self.require_trusted = require_trusted
        self.verbose = verbose

    def path_to_url(self, path):
        if path.startswith("/"):
            return self.url + path
        else:
            return self.url + "/securesync/api/" + path

    def post(self, path, payload={}, *args, **kwargs):

        from kalite.version import user_agent

        if self.verbose:
            print "CLIENT: post %s" % path
        return requests.post(
            self.path_to_url(path),
            data=json.dumps(payload),
            headers={"user-agent": user_agent()}
        )

    def get(self, path, payload={}, *args, **kwargs):

        from kalite.version import user_agent

        # add a random parameter to ensure the request is not cached
        payload["_"] = uuid.uuid4().hex
        query = urllib.urlencode(payload)
        if self.verbose:
            logging.debug("CLIENT: get %s" % path)
        kwargs['headers'] = kwargs.get('headers', {})
        kwargs['headers']["user-agent"] = user_agent()
        return requests.get(
            self.path_to_url(path) + "?" + query,
            *args,
            **kwargs
        )

    def test_connection(self):
        try:
            if self.get("test", timeout=5).content != "OK":
                return "bad_address"
            return "success"
        except requests.ConnectionError:
            return "connection_error"
        except Exception as e:
            return "error (%s)" % e
