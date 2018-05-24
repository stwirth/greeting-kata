import unittest

from greet import greet

class GreetTest(unittest.TestCase):

    def test_greet(self):
        self.assertEqual(greet('Bob'), 'Hello, Bob.')
