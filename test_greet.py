import unittest

from greet import greet

class GreetTest(unittest.TestCase):

    def test_greet(self):
        self.assertEqual(greet('Bob'), 'Hello, Bob.')

    def test_null_name(self):
        self.assertEqual(greet(None), 'Hello, my friend.')
