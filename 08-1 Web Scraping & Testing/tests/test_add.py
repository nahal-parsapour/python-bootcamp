import unittest
import importlib

module = importlib.import_module("src.13AddDefForTest")

add = module.add
is_even = module.is_even



class TestFunctions(unittest.TestCase):

    def test_add_success(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_failure(self):
        self.assertNotEqual(add(2, 2), 5)

    def test_is_even_success(self):
        self.assertTrue(is_even(4))

    def test_is_even_failure(self):
        self.assertFalse(is_even(5))

    def test_add_negative(self):
        self.assertEqual(add(-2, -5), -7)

    def test_add_zero(self):
        self.assertEqual(add(0, 5), 5)

    def test_is_even_zero(self):
        self.assertTrue(is_even(0))


if __name__ == '__main__':
    unittest.main()