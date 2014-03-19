import unittest

from ..client import Client


class TestClient(unittest.TestCase):

    def setUp(self):
        self.client_username = "username"
        self.client_password = "password"
        self.client_product = "product"
        self.client = Client(
            self.client_username,
            self.client_password,
            self.client_product
        )

    def test_request(self):
        pass

    def test_client_has_methods(self):
        """ Test method created with metaclass."""
        self.assertTrue(hasattr(self.client, "get_all_pricing_plans"))
        self.assertFalse(hasattr(self.client, "get_a_single_pricing_plan"))
        self.assertTrue(hasattr(self.client, "get_single_pricing_plan"))

    def test_get_all_pricing_plans__doc__(self):
        self.assertEqual(
            self.client.get_all_pricing_plans.__doc__,
            "Get all pricing plan data from the product with " +
            "productCode={}".format(self.client_product)
        )
