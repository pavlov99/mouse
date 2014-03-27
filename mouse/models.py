""" Cheddargetter models used in framework."""
from hashlib import md5
from collections import namedtuple
from . import six


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
        CHEDDARGETTER_PASSWORD = "*"
        key = md5("{}|{}".format(
            self.code, CHEDDARGETTER_PASSWORD)).\
            hexdigest()[:KEY_LENGTH]
        return key
