from lookout.base import ServiceBase
import simplejson as json
import urllib2


class Service(ServiceBase):
    """
    WebHooks

    We'll hit these URLs with a POST request when a new piece of data is created
    within your Sprint.ly project.
    """
    def send(self, payload):
        try:
            urls = self.options['urls']
        except KeyError:
            return  # Nothing to do here.

        data = json.dumps(payload)
        headers = {
            'Content-Type': 'application/json',
            'Content-Length': len(data)
        }

        for url in urls:
            request = urllib2.Request(url, data, headers)
            fp = urllib2.urlopen(request, timeout=2)
            fp.close()
