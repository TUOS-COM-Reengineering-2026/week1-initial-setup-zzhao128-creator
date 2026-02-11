import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import hello


class TestAutograder(unittest.TestCase):
    def test_result(self):
        # check if the file `causal_testing.png` exists
        self.assertEqual("Hello Reengineering", hello.say_hello())
