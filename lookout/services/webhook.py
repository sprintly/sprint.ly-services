import urllib2
import simplejson as json

from lookout.base import ServiceBase


class Service(ServiceBase):
    """
    WebHooks

    We'll hit these URLs with a POST request when a new piece of data is created
    within your Sprint.ly project. More information on what we send and in what
    format can be found in our [WebHooks Guide](https://support.sprint.ly/hc/en-us/articles/213646967-WebHooks-Guide).
    """
    def send(self, payload):
        try:
            urls = self.options['urls']
        except KeyError:
            return  # Nothing to do here.

        for url in urls:
            self._request(url, payload)

    def _request(self, url, data):
        payload = json.dumps(data)

        headers = {
            'Content-Type': 'application/json',
            'Content-Length': len(payload)
        }
        
        request = urllib2.Request(url, payload, headers)
        fp = urllib2.urlopen(request, timeout=2)
        fp.close()
