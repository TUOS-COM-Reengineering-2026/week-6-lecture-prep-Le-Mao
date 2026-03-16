import unittest
from prep import strange_function

class MyTestCase(unittest.TestCase):
    def test_strange_function1(self):
        self.assertEqual(
            first=strange_function(1, 2, 3, 4),
            second='behaviour 3'
        )

    # TODO: Can you write more test cases below to increase the test coverage of `strange_function`?

    def test_strange_function2(self):
        # a == b; c < d
        self.assertEqual(
            strange_function("hello", "hello", 1, 4),
            'behaviour 1'
        )
    
    
    def test_strange_function3(self):
        # a == b; c >= d
        self.assertEqual(
            strange_function(0, 0, 0.5, 0.5),
            'behaviour 2'
        )
    
    def test_strange_function4(self):
        # a != b; a >= c; d < b
        self.assertEqual(
            strange_function(0, 1, 0, 0),
            'behaviour 4'
        )

    def test_strange_function5(self):
        # a != b; a >= c; d >= b; c < a
        self.assertEqual(
            strange_function(0, 1, -1, 1),
            'behaviour 5'
        )

    def test_strange_function6(self):
        # a != b; a >= c; d >= b; c >= a
        self.assertEqual(
            strange_function(0, 1, 0, 1),
            'behaviour 6'
        )