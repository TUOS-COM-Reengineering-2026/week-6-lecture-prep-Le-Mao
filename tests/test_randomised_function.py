import unittest
from lecture import randomised_function

class MyTestCase(unittest.TestCase):

    def test_randomised_function(self):
        self.assertTrue(randomised_function() in "software engineering")  # This will pass or fail randomly
        # TODO: Can we make this test deterministic? (HINT: Mock testing)
