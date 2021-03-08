import unittest
import leapyear
class TestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(leapyear.code(4), True)

unittest.main()