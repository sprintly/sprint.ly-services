from lookout.base import ServiceBase
import requests
import re


class Service(ServiceBase):
    """
    Flowdock

    This will send events from Sprint.ly to your Flowdock Team Inbox. To install
    the package follow the steps below:

    1. `auth_token` is the API token for the flow you would like to post to. You can find your flow API tokens at `https://www.flowdock.com/account/tokens`
    """
    RE_STRICT = re.compile('[^a-zA-Z0-9\s_]+')

    def _strip(self, text):
        return self.RE_STRICT.sub('_', text)

    def send(self, payload):
        if payload['model'] == 'Comment':
            subject = 'commented on %s "%s" in %s' % (
                payload['attributes']['item']['type'],
                payload['attributes']['item']['title'],
                payload['product']['name'],
            )
            message = '"%s"' % (
                payload['attributes']['body']
            )

            data = {
                'source': 'Sprintly',
                'from_address': payload['attributes']['item']['email']['discussion'],
                'subject': subject,
                'content': message,
                'from_name': '%s %s' % (payload['attributes']['created_by']['first_name'], payload['attributes']['created_by']['last_name']),
                'project': self._strip(payload['product']['name']),
                'format': 'html',
                'tags': payload['attributes']['item']['tags'],
                'link': payload['attributes']['item']['short_url']
            }

        elif payload['model'] == 'Item':
            subject = 'New %s "%s" (#%d) in %s' % (
                payload['attributes']['type'],
                payload['attributes']['title'],
                payload['attributes']['number'],
                payload['product']['name'],
            )

            message = '%s %s. created %s "%s"' % (
                payload['attributes']['created_by']['first_name'],
                payload['attributes']['created_by']['last_name'],
                payload['attributes']['type'],
                payload['attributes']['title'],
            )
            if payload['attributes']['assigned_to'] and \
                payload['attributes']['assigned_to']['id'] != \
                payload['attributes']['created_by']['id']:
                message += ' and assigned it to %s %s.' % (
                    payload['attributes']['assigned_to']['first_name'],
                    payload['attributes']['assigned_to']['last_name'])
            if payload['attributes']['description'] is not None and len(payload['attributes']['description']):
                message += '<p><blockquote>"%s"</blockquote></p>' % payload['attributes']['description']

            data = {
                'source': 'Sprintly',
                'from_address': payload['attributes']['email']['discussion'],
                'subject': subject,
                'content': message,
                'from_name': '%s %s' % (payload['attributes']['created_by']['first_name'], payload['attributes']['created_by']['last_name']),
                'project': self._strip(payload['product']['name']),
                'format': 'html',
                'tags': payload['attributes']['tags'],
                'link': payload['attributes']['short_url']
            }

        elif payload['model'] == 'Block':
            subject = '%s %s "%s" is blocking %s "%s"' % (
                payload['product']['name'],
                payload['attributes']['item']['type'],
                payload['attributes']['item']['title'],
                payload['attributes']['blocked']['type'],
                payload['attributes']['blocked']['title'],
            )

            message = '%s %s. indicated %s "%s" in %s' % (
                payload['attributes']['user']['first_name'],
                payload['attributes']['user']['last_name'],
                payload['attributes']['item']['type'],
                payload['attributes']['item']['title'],
                payload['product']['name'],
            )
            if payload['attributes']['item']['assigned_to']:
                message += ' (assigned to %s %s.)' % (
                    payload['attributes']['item']['assigned_to']['first_name'],
                    payload['attributes']['item']['assigned_to']['last_name'],
                )
            message += ' is blocking %s "%s"' % (
                payload['attributes']['blocked']['type'],
                payload['attributes']['blocked']['title'],
            )

            data = {
                'source': 'Sprintly',
                'from_address': payload['attributes']['item']['email']['discussion'],
                'subject': subject,
                'content': message,
                'from_name': '%s %s' % (payload['attributes']['user']['first_name'], payload['attributes']['user']['last_name']),
                'project': self._strip(payload['product']['name']),
                'format': 'html',
                'tags': payload['attributes']['item']['tags'],
                'link': payload['attributes']['item']['short_url']
            }

        elif payload['model'] == 'Favorite':
            message = '%s %s. favorited %s "%s" in %s' % (
                payload['attributes']['user']['first_name'],
                payload['attributes']['user']['last_name'],
                payload['attributes']['item']['type'],
                payload['attributes']['item']['title'],
                payload['product']['name'],
            )

            data = {
                'source': 'Sprintly',
                'from_address': payload['attributes']['item']['email']['discussion'],
                'subject': message,
                'content': message,
                'from_name': '%s %s' % (payload['attributes']['user']['first_name'], payload['attributes']['user']['last_name']),
                'project': self._strip(payload['product']['name']),
                'format': 'html',
                'tags': payload['attributes']['item']['tags'],
                'link': payload['attributes']['item']['short_url']
            }

        elif payload['model'] == 'Deploy':
            subject = '%s %s. deployed %s items in %s to %s' % (
                payload['attributes']['user']['first_name'],
                payload['attributes']['user']['last_name'],
                len(payload['attributes']['items']),
                payload['product']['name'],
                payload['attributes']['environment']
            )

            message = '%s release notes:\n<ul>' % payload['attributes']['environment'].capitalize()
            for item in payload['attributes']['items']:
                message += '<li><a href="%s">%s #%d</a>: %s</li>' % (
                    item['short_url'],
                    item['type'].capitalize(),
                    item['number'],
                    item['title'],
                )
            message += '</ul>'

            data = {
                'source': 'Sprintly',
                'from_address': payload['attributes']['user']['created_by']['email'],
                'subject': subject,
                'content': message,
                'project': self._strip(payload['product']['name']),
                'format': 'html'
            }
        else:
            message = None
        if not message:
            return

        url = "https://api.flowdock.com/v1/messages/team_inbox/%s" % str(self.options['auth_token'])
        r = requests.post(url, data=data)
