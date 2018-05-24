import unittest

from greet import greet

class GreetTest(unittest.TestCase):

    def test_greet(self):
        self.assertEqual(greet('Bob'), 'Hello, Bob.')

    def test_null_name(self):
        self.assertEqual(greet(None), 'Hello, my friend.')

    def test_shout(self):
        self.assertEqual(greet('JERRY'), 'HELLO JERRY!')

    def test_greet_two_names(self):
        self.assertEqual(greet(['Jill', 'Jane']), 'Hello, Jill and Jane.')
