from lookout.services.webhook import Service as WebHookService
from lookout.base import MessageServiceBase

class Service(WebHookService, MessageServiceBase):
    """
    Slack

    This will send item events from Sprint.ly to Slack. Simply configure an
    incoming WebHook for your Slack account here.
    """
    def send(self, payload):
        payload['text'] = self.message(payload)
        super(WebHookService, self).send(payload)
