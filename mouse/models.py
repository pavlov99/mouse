""" Cheddargetter models used in framework."""
from hashlib import md5


class Customer(object):
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
