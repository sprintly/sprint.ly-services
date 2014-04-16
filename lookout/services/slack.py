from lookout.services.webhook import Service as WebHookService
from lookout.base import SPRINTLY_DEFAULT_COLOR, SPRINTLY_COLORS, MessageServiceBase

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

        data = self.get_post_data(payload)

        if options:
            data.update(options)

        self._request(url, data)

    def get_post_data(self, data):
        """
        Take payload data and format it appropriately to post to Slack
        """

        # Set default data 

        message = MessageServiceBase.message(data)

        default_data = {
            'color': SPRINTLY_DEFAULT_COLOR,
            'fallback': message,
            'pretext': message
        }

        # Get activity model-specific data-grabber method name and call it

        format_method = 'get_%s_attachment' % data['model'].lower()
        attachment = getattr(self, format_method, lambda data: None)(data)

        # Merged returned data with default
        
        default_data.update(attachment)

        return {'attachments': [default_data]}

    def get_attachment_color(self, item_data=None):
        """
        Get attachment color
        """
        return SPRINTLY_COLORS[item_data.get('type') if item_data else None]



    # comment, block, item, favorite, deply

    def get_block_attachment(self, data):
        """
        x indicated item y is blocked by item z, which is assigned to j
        (include item )
        """
        pass

    def get_comment_attachment(self, data):
        pass

    def get_deploy_attachment(self, data):
        pass

    def get_favorite_attachment(self, data):
        pass

    def get_item_attachment(self, data):
        item = data['attributes']

        attachment = {
            'color': self.get_attachment_color(item),
            'text': '<%s|#%s> %s' % (item['short_url'], item['number'], item['title']),
            'fields': []
        }

        if item['assigned_to']:
            attachment['fields'].append({
                'title': 'Assigned to',
                'value': '%s' % MessageServiceBase.format_name(item['assigned_to']),
                'short': True
            })

        if item['status']:
            attachment['fields'].append({
                'title': 'Status',
                'value': ' '.join(item['status'].split('-')).capitalize(),
                'short': True
            })

        if item['score']:
            attachment['fields'].append({
                'title': 'Score',
                'value': item['score'],
                'short': True
            })

        return attachment
