from decorator import decorator
import re


def listen_to(*patterns):
    pattern = '^(%s)$' % '|'.join([p.replace('.', '\.').replace('*', '\w+') for p in patterns])
    matcher = re.compile(pattern)

    @decorator
    def __wrapped__(f, *args, **kwargs):
        try:
            action = args[1]['action']
        except IndexError:
            return  # No payload argument?
        except KeyError:
            action = 'created'

        try:
            model = args[1]['model']
        except KeyError:
            return  # Weird payload argument?

        model_action = '%s.%s' % (model, action)
        if not matcher.match(model_action):
            return  # Model/action not tracked by this function.

        return f(*args, **kwargs)

    return __wrapped__
