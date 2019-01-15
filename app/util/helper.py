# ROLE_ADMIN = 'admin'
# ROLE_USER = 'user'


class Message(object):
    dont_have_permission: str = "You don't have permission"


def log(msg):
    from django.conf import settings
    if hasattr(settings, 'DEBUG') and getattr(settings, 'DEBUG'):
        import inspect
        print(f"{inspect.stack()[1][1]}:{inspect.stack()[1][2]} {msg}")
