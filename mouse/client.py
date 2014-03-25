""" Client implementation."""
from requests.auth import HTTPBasicAuth
import logging
import requests

from .settings import REQUEST_MAP
from .utils import get_string_kwargs, FrozenDict, get_partly_formated_string

logger = logging.getLogger(__name__)


class Client(object):

    """ Api client implementation."""

    BASE_URL = "https://cheddargetter.com/xml"
    REQUEST_MAP = FrozenDict([
        (
            method["title"].replace(" a ", " ").replace(" ", "_").lower(),
            method
        ) for method in REQUEST_MAP
    ])

    def __init__(self, username, password, product_code):
        self.username = username
        self.password = password
        self.product_code = product_code

    def request(self, method, path, **params):
        # TODO: exception handler
        url = self.BASE_URL + path
        logger.debug("Call {}: {} with params {}".format(method, url, params))
        print("Call {}: {} with params {}".format(method, url, params))
        response = requests.request(
            method,
            url,
            params=params,
            auth=HTTPBasicAuth(self.username, self.password)
        )
        #response.raise_for_status()
        return response

    @property
    def methods(self):
        """ Return available methods."""
        return sorted(self.REQUEST_MAP.keys())

    def __getattr__(self, method_name):
        if method_name in self.REQUEST_MAP:
            method = self.REQUEST_MAP[method_name]
            path = get_partly_formated_string(
                method["path"], {"product_code": self.product_code})
            path_template = path.format(**{
                x: "{" + str(i) + "}"
                for i, x in enumerate(get_string_kwargs(path))
            })

            f = lambda *args, **kwargs: self.request(
                method["request_method"],
                path_template.format(*args),
                **kwargs
            )
            f.__name__ = method_name
            f.__doc__ = get_partly_formated_string(
                method["doc"], {"product_code": self.product_code})
            return f
        else:
            return super(Client, self).__getattr__(method_name)
