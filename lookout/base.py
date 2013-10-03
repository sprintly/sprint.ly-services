import os
from django.utils.importlib import import_module


class ServiceBase(object):
    def __init__(self, options):
        self.options = options

    def send(self, payload):
        raise NotImplementedError

    @property
    def name(self):
        return self.__class__.__module__.split('.')[-1]

    @property
    def title(self):
        return self.__doc__.split('\n')[1].strip()

    @property
    def description(self):
        return '\n'.join([l.strip() for l in self.__doc__.split('\n')[2:]]).strip()

class MessageServiceBase(ServiceBase):
    def message(payload):
        model = payload['model']
        attr = payload['attributes']
        if payload['model'] == 'Comment':
            message = '%s %s. commented "%s" on %s "%s" (#%s) %s' % (
                attr['created_by']['first_name'],
                attr['created_by']['last_name'][0],
                '%s...' % self._clean_mentions(attr['body'])[0:50],
                attr['item']['type'],
                attr['item']['title'],
                attr['item']['number'],
                attr['item']['short_url'])
        elif model == 'Item':
            message = '%s %s. created the %s "%s" (#%s) %s' % (
                attr['created_by']['first_name'],
                attr['created_by']['last_name'][0],
                attr['type'],
                attr['title'],
                attr['number'],
                attr['short_url'])

            if attr['assigned_to'] and \
                attr['assigned_to']['id'] != \
                attr['created_by']['id']:
                message += ' and assigned it to %s %s.' % (
                    attr['assigned_to']['first_name'],
                    attr['assigned_to']['last_name'][0])
        elif model == 'Block':
            message = '%s %s. indicated the %s "%s" (#%s) %s is blocked on the %s "%s" (#%s) %s' % (
                attr['user']['first_name'],
                attr['user']['last_name'][0],
                attr['blocked']['type'],
                attr['blocked']['title'],
                attr['blocked']['number'],
                attr['blocked']['short_url'],
                attr['item']['type'],
                attr['item']['title'],
                attr['item']['number'],
                attr['item']['short_url'])

            if attr['item']['assigned_to']:
                message += ', which is owned by %s %s.' % (
                    attr['item']['assigned_to']['first_name'],
                    attr['item']['assigned_to']['last_name'][0])
        elif model == 'Favorite':
            message = '%s %s. favorited the %s "%s" (#%s) %s' % (
                attr['user']['first_name'],
                attr['user']['last_name'][0],
                attr['item']['type'],
                attr['item']['title'],
                attr['item']['number'],
                attr['item']['short_url'])
        elif model == 'Deploy':
            message = '%s %s. deployed %s items to %s.' % (
                attr['user']['first_name'],
                attr['user']['last_name'][0],
                len(attr['items']),
                attr['environment'])
        else:
            message = None
        return message

def get_available_services():
    path = '%s/services' % os.path.dirname(__file__)
    services = {}
    for service_file in os.listdir(path):
        if service_file.endswith('.pyc') or service_file.startswith('__') or \
            service_file.startswith('.'):
            continue

        service_name = service_file.split('.')[0]
        if not service_name:
            continue

        try:
            module = import_module('lookout.services.%s' % service_name)
            services[service_name] = module.Service
        except ImportError:
            continue

    return services
