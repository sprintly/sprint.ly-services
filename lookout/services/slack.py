from lookout.services.webhook import Service as WebHookService

class Service(WebHookService):
    """
    Slack

    This will send item events from Sprint.ly to Slack. Simply configure an
    incoming WebHook for your Slack account here.
    """
    def send(self, payload):
        options = self.options.copy()

        try:
            url = options.pop('url')
        except KeyError:
            return

        data = {'text': self.get_message(payload)}

        if options:
            data.update(options)

        self._request(url, data)
