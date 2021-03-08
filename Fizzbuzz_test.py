import unittest
import fizzbuzz
class TestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(fizzbuzz.code(5), "Fizz")

unittest.main()