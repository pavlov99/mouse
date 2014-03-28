from . import six


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(
                *args, **kwargs)
        return cls._instances[cls]


@six.add_metaclass(Singleton)
class CheddargetterSettings(object):
    pass

settings = CheddargetterSettings()
settings.USERNAME = ""
settings.PASSWORD = ""
settings.PRODUCT_CODE = ""
settings.BASE_URL = "https://mouse.chargevault.com"
