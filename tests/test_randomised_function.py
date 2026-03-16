import unittest
from unittest.mock import patch
from lecture import randomised_function

class MyTestCase(unittest.TestCase):

    def test_randomised_function(self):
        self.assertTrue(randomised_function() in "software engineering")  # This will pass or fail randomly
        # TODO: Can we make this test deterministic? (HINT: Mock testing)

    @patch('random.randint')
    def test_randomised_function_mocked(self, mock_rand):
        mock_rand.return_value = 3 # small
        self.assertEqual('software', randomised_function())

        mock_rand.return_value = 7 # not small
        self.assertEqual('engineering', randomised_function())
