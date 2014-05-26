""" Cheddargetter models used in framework."""
from collections import namedtuple
from hashlib import md5
import requests

try:
    from urllib import urlencode
except ImportError:
    from urllib.parse import urlencode


from . import six
from .settings import settings
from .client import Client
from .utils import namedtuple_as_dict, classproperty


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
        class_name = str(class_name)
        cls_mixin_name = class_name + "Mixin"
        cls_mixin = FactoryMeta.__store__.get(cls_mixin_name, object)
        cls_base = namedtuple(class_name, kwargs.keys())
        methods = {"as_dict": property(namedtuple_as_dict)}
        cls = type(class_name, (cls_base, cls_mixin), methods)
        return cls(**kwargs)


class ClientMixin(object):
    @classproperty
    @classmethod
    def client(cls):
        return Client(
            settings.USERNAME,
            settings.PASSWORD,
            settings.PRODUCT_CODE
        )


@six.add_metaclass(FactoryMeta)
class CustomerMixin(ClientMixin):
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

    @property
    def status(self):
        """ Return Customer status.

        http://support.cheddargetter.com/kb/hosted-payment-pages/
            hosted-payment-pages-setup-guide#status
        :return str status: ('active'|'canceled'|'pending')
        """
        return requests.get(self.status_url, verify=False).content

    @classmethod
    def get_all(cls):
        return cls.client.get_all_customers()

    def delete(self):
        return self.client.delete_customer(self.code)
