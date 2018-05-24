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

    def test_greet_multiple(self):
        self.assertEqual(greet(['Amy', 'Brian', 'Charlotte']),
                         'Hello, Amy, Brian, and Charlotte.')

    def test_mix_shouting(self):
        self.assertEqual(greet(['Amy', 'BRIAN', 'Charlotte']),
                         'Hello, Amy and Charlotte. AND HELLO BRIAN!')

    def test_split_comma(self):
        self.assertEqual(greet(['Bob', 'Charlie, Dianne']),
                         'Hello, Bob, Charlie, and Dianne.')

    def test_intentional_comma(self):
        self.assertEqual(greet(['Bob', '"Charlie, Dianne"']),
                         'Hello, Bob and Charlie, Dianne.')
