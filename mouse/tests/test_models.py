from ..models import Factory
import unittest


class TestFactory(unittest.TestCase):
    def test_instantiate_class_name(self):
        Factory.instantiate("Customuser")
