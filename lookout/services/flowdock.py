from lookout.base import ServiceBase
import requests

class Service(ServiceBase):
    """
    Flowdock

    This will send events from Sprint.ly to Flowdock Team Inbox!
    
    1. `auth_token` this is the api token for the particular flow you'd like to post to.
    """
    def send(self, payload):
        if payload['model'] == 'Comment':
            message = '%s %s. commented "%s" on %s "%s" (#%s) %s' % (
                payload['attributes']['created_by']['first_name'],
                payload['attributes']['created_by']['last_name'][0],
                '%s...' % payload['attributes']['body'], 
                payload['attributes']['item']['type'],
                payload['attributes']['item']['title'],
                payload['attributes']['item']['number'],
                payload['attributes']['item']['short_url'])

            data = {
                'source': 'Sprint.ly',
                'from_address': payload['attributes']['created_by']['email'],
                'subject' : payload['attributes']['item']['title'],
                'content' : message,
                'from_name' : payload['attributes']['created_by']['first_name'] + payload['attributes']['created_by']['last_name'][0],
                'project' : payload['product']['name'],
                'format' : 'html',
                'tags' : payload['attributes']['item']['tags'],
                'link' : payload['attributes']['item']['short_url']
            }

        elif payload['model'] == 'Item':
            message = '%s %s. created the %s "%s" (#%s) %s' % (
                payload['attributes']['created_by']['first_name'],
                payload['attributes']['created_by']['last_name'][0],
                payload['attributes']['type'],
                payload['attributes']['title'],
                payload['attributes']['number'],
                payload['attributes']['short_url'])

            if payload['attributes']['assigned_to'] and \
                payload['attributes']['assigned_to']['id'] != \
                payload['attributes']['created_by']['id']:
                message += ' and assigned it to %s %s.' % (
                    payload['attributes']['assigned_to']['first_name'],
                    payload['attributes']['assigned_to']['last_name'][0])


            data = {
                'source': 'Sprint.ly',
                'from_address': payload['attributes']['created_by']['email'],
                'subject' : payload['attributes']['title'],
                'content' : message,
                'from_name' : payload['attributes']['created_by']['first_name'] + payload['attributes']['created_by']['last_name'][0],
                'project' : payload['product']['name'],
                'format' : 'html',
                'tags' : payload['attributes']['tags'],
                'link' : payload['attributes']['short_url']
            }


        elif payload['model'] == 'Block':
            message = '%s %s. indicated the %s "%s" (#%s) %s is blocked on the %s "%s" (#%s) %s' % (
                payload['attributes']['user']['first_name'],
                payload['attributes']['user']['last_name'][0],
                payload['attributes']['blocked']['type'],
                payload['attributes']['blocked']['title'],
                payload['attributes']['blocked']['number'],
                payload['attributes']['blocked']['short_url'],
                payload['attributes']['item']['type'],
                payload['attributes']['item']['title'],
                payload['attributes']['item']['number'],
                payload['attributes']['item']['short_url'])

            if payload['attributes']['item']['assigned_to']:
                message += ', which is owned by %s %s.' % (
                    payload['attributes']['item']['assigned_to']['first_name'],
                    payload['attributes']['item']['assigned_to']['last_name'][0])

            data = {
                'source': 'Sprint.ly',
                'from_address': payload['attributes']['created_by']['email'],
                'subject' : payload['attributes']['blocked']['title'],
                'content' : message,
                'from_name' : payload['attributes']['blocked']['created_by']['first_name'] + payload['attributes']['blocked']['created_by']['last_name'][0],
                'project' : payload['product']['name'],
                'format' : 'html',
                'tags' : payload['attributes']['tags'],
                'link' : payload['attributes']['short_url']
            }

        elif payload['model'] == 'Favorite':
            message = '%s %s. favorited the %s "%s" (#%s) %s' % (
                payload['attributes']['user']['first_name'],
                payload['attributes']['user']['last_name'][0],
                payload['attributes']['item']['type'],
                payload['attributes']['item']['title'],
                payload['attributes']['item']['number'],
                payload['attributes']['item']['short_url'])

            data = {
                'source': 'Sprint.ly',
                'from_address': payload['attributes']['user']['created_by']['email'],
                'subject' : payload['attributes']['item']['title'],
                'content' : message,
                'from_name' : payload['attributes']['user']['created_by']['first_name'] + payload['attributes']['user']['created_by']['last_name'][0],
                'project' : payload['product']['name'],
                'format' : 'html',
                'tags' : payload['attributes']['tags'],
                'link' : payload['attributes']['short_url']
            }


        elif payload['model'] == 'Deploy':
            message = '%s %s. deployed %s items to %s.' % (
                payload['attributes']['user']['first_name'],
                payload['attributes']['user']['last_name'][0],
                len(payload['attributes']['items']),
                payload['attributes']['environment'])

            

            #I'm not sure on the docs on this one?

            data = {
                'source': 'Sprint.ly',
                'from_address': payload['attributes']['user']['created_by']['email'],
                'subject' : payload['attributes']['item']['title'],
                'content' : message,
                'format' : 'html'
            }

        else:
            message = None

        if not message:
            return
        
        r = requests.post("https://api.flowdock.com/v1/messages/team_inbox/" + self.options['auth_token'], data=data)