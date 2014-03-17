""" Client implementation."""
from requests.auth import HTTPBasicAuth
import logging
import requests

logger = logging.getLogger(__name__)


class Client(object):

    """ Api client implementation."""

    BASE_URL = "https://cheddargetter.com/xml/{path}/productCode/" +\
        "{product_code}"

    def __init__(self, username, password, product_code):
        self.username = username
        self.password = password
        self.product_code = product_code
        self.base_url = self.BASE_URL.format(product_code=product_code)

    def request(self, path, params, method=None):
        method = method or "GET"
        url = self.base_url.format(path=path)
        response = requests.request(
            method,
            url,
            params=params,
            auth=HTTPBasicAuth(self.username, self.password)
        )
        return response
