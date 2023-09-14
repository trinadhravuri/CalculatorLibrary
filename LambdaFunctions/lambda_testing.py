"""
* Lambda functions can be tested similarly to regular functions.
* unittest handles lambda functions in a similar manner to regular functions.
"""

import unittest


squared = lambda x:x ** 2

class LambdaTest(unittest.TestCase):

    def test_squared(self):
        self.assertEqual(squared(2),4)

    def test_zero(self):
        self.assertEqual(squared(0),0)

    def test_negative(self):
        self.assertEqual(squared(-3),9)

if __name__ == "__main__":
    unittest.main(verbosity=2)
