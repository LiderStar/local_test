from unittest import TestCase
from store.logic import operation


class LogicTestCase(TestCase):
    def test_plus(self):
        result = operation(3, 6, '+')
        self.assertEqual(9, result)

    def test_minus(self):
        result = operation(7, 3, '-')
        self.assertEqual(4, result)