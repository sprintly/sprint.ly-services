from lookout.services.webhook import Service as WebHookService
from lookout.base import SPRINTLY_DEFAULT_COLOR, SPRINTLY_COLORS, MessageServiceBase
from lookout.decorators import listen_to


class Service(WebHookService):
    """
    Slack

    This will send item events from Sprint.ly to Slack. Simply configure an
    incoming WebHook for your Slack account here.

    Visit the following URL for Slack configuration documentation:
    `https://my.slack.com/services/new/incoming-webhook`
    """
    @listen_to('*.created')
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
            'fallback': message
        }

        # Get activity model-specific attachment data-formatting method name and call it

        format_method = 'get_%s_attachment' % data['model'].lower()
        attachment = getattr(self, format_method, lambda data: None)(data)

        # Merged returned data with default
        
        default_data.update(attachment)

        return {
            'icon_url': 'https://s3.amazonaws.com/sprintly-marketing-assets/integrations/slack-bot-icon.png',
            'attachments': [default_data]
        }

    def get_attachment_color(self, item_data=None):
        """
        Get attachment color
        """
        return SPRINTLY_COLORS[item_data.get('type') if item_data else None]

    def get_block_attachment(self, data):
        """
        Return a dict with attachment data for Block activity
        """
        block = data['attributes']
        attachment = self.extract_item_attachment_data(block['item'])
        attachment['pretext'] = '%s indicated the %s %s is blocked by the %s:' % (
            MessageServiceBase.format_name(block['user']),
            block['blocked']['type'],
            self.format_item_link(block['blocked']),
            block['item']['type']
        )
        return attachment

    def get_comment_attachment(self, data):
        """
        Return a dict with attachment data for Comment activity
        """
        comment = data['attributes']
        pretext = '%s commented on %s %s:' % (
            MessageServiceBase.format_name(comment['created_by']),
            comment['item']['type'],
            self.format_item_link(comment['item'])
        )
        return {
            'color': self.get_attachment_color(comment['item']),
            'pretext': pretext,
            'text': '"%s"' % MessageServiceBase.format_comment(comment['body'])
        }

    def get_deploy_attachment(self, data):
        """
        Return a dict with attachment data for Deploy activity
        """
        deploy = data['attributes']
        items = deploy['items']
        return {
            'color': self.get_attachment_color(),
            'text': '%s deployed %d item%s to %s' % (
                MessageServiceBase.format_name(deploy['user']),
                len(items),
                '' if len(items) == 1 else 's',
                deploy['environment']
            )
        }

    def get_favorite_attachment(self, data):
        """
        Return a dict with attachment data for Favorite activity
        """
        fave = data['attributes']
        attachment = self.extract_item_attachment_data(fave['item'])
        attachment['pretext'] = '%s favorited the %s:' % (
            MessageServiceBase.format_name(fave['user']),
            fave['item']['type']
        )
        return attachment

    def get_item_attachment(self, data):
        """
        Return a dict with attachment data for Item activity
        """
        item = data['attributes']
        attachment = self.extract_item_attachment_data(item)
        attachment['pretext'] = '%s created the %s:' % (MessageServiceBase.format_name(item['created_by']), item['type'])
        return attachment

    def extract_item_attachment_data(self, item):
        """
        Extract item data from passed in item dict for use in an attachment
        """
        item_attachment = {
            'color': self.get_attachment_color(item),
            'text': self.format_item_link(item),
            'fields': []
        }

        if item['assigned_to']:
            item_attachment['fields'].append({
                'title': 'Assigned to',
                'value': '%s' % MessageServiceBase.format_name(item['assigned_to']),
                'short': True
            })

        if item['status']:
            item_attachment['fields'].append({
                'title': 'Status',
                'value': ' '.join(item['status'].split('-')).capitalize(),
                'short': True
            })

        if item['score']:
            item_attachment['fields'].append({
                'title': 'Score',
                'value': item['score'],
                'short': True
            })

        return item_attachment

    def format_item_link(self, item):
        """
        Use the passed in dict of item data and return a Slack-formatted URL string 
        for it with item number and title
        """
        return '<%s|#%s - %s>' % (
            item['short_url'],
            item['number'],
            item['title']
        )
