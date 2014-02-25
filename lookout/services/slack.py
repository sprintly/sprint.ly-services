from lookout.services.webhook import Service as WebHookService
from lookout.base import MessageServiceBase

class Service(WebHookService):
    """
    Slack

    This will send item events from Sprint.ly to Slack. Simply configure an
    incoming WebHook for your Slack account here.

    Visit the following URL for Slack configuration documentation:
    `https://my.slack.com/services/new/incoming-webhook`
    """
    def send(self, payload):
        options = self.options.copy()

        try:
            url = options.pop('url')
        except KeyError:
            return

        data = {'text': MessageServiceBase.message(payload)}

        if options:
            data.update(options)

        self._request(url, data)
