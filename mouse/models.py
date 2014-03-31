""" Cheddargetter models used in framework."""
from collections import namedtuple
from hashlib import md5

try:
    from urllib import urlencode
except ImportError:
    from urllib.parse import urlencode


from . import six
from .settings import settings


class FactoryMeta(type):

    """ Proxy objects metaclass. """

    __store__ = dict()

    def __new__(class_, name, bases, params):
        cls = super(FactoryMeta, class_).__new__(class_, name, bases, params)
        class_.__store__[name] = cls
        return cls


class Factory(object):
    @staticmethod
    def instantiate(class_name, **kwargs):
        cls_mixin_name = str(class_name) + "Mixin"
        cls_mixin = FactoryMeta.__store__.get(cls_mixin_name, object)
        cls_base = namedtuple(class_name, kwargs.keys())
        return type(class_name, (cls_base, cls_mixin), {})(**kwargs)


@six.add_metaclass(FactoryMeta)
class CustomerMixin(object):
    @property
    def key(self):
        """ Customer key used in url links.

        The Customer Key is a hash of the Customer Code and your Product
        Secret Key. Customers will also be able to update their data through
        links. Some of the links should have customer key as a parameter.

        :return str: customer key

        """
        KEY_LENGTH = 10
        key = md5("{}|{}".format(
            self.code, settings.PASSWORD)).\
            hexdigest()[:KEY_LENGTH]
        return key

    @property
    def create_url(self):
        params = urlencode(dict(code=self.code)) if hasattr(self, "code") \
            else ""
        url = "{}/create?{}".format(settings.BASE_URL, params)
        return url

    @property
    def update_url(self):
        params = urlencode(dict(key=self.key, code=self.code))
        url = "{}/update?{}".format(settings.BASE_URL, params)
        return url

    @property
    def cancel_url(self):
        params = urlencode(dict(key=self.key, code=self.code))
        url = "{}/cancel?{}".format(settings.BASE_URL, params)
        return url

    @property
    def status_url(self):
        params = urlencode(dict(key=self.key, code=self.code))
        url = "{}/status?{}".format(settings.BASE_URL, params)
        return url
