import unittest
import sys
import os
import importlib.util

file_path = os.path.join(os.path.dirname(__file__), '..', 'src', '06RewriteEx3_price-utils.py')
spec = importlib.util.spec_from_file_location("price_utils", file_path)
price_utils = importlib.util.module_from_spec(spec)
spec.loader.exec_module(price_utils)



class TestPriceUtils(unittest.TestCase):

    def test_convert_price_to_float_standard(self):
        self.assertAlmostEqual(price_utils.convert_price_to_float("£51.77"), 51.77)
        self.assertAlmostEqual(price_utils.convert_price_to_float("$1,999.20"), 1999.20)
        self.assertAlmostEqual(price_utils.convert_price_to_float("€500"), 500.0)
        self.assertAlmostEqual(price_utils.convert_price_to_float("   ฿5.45   "), 5.45)
        self.assertEqual(price_utils.convert_price_to_float(""), 0.0)

if __name__ == '__main__':
    unittest.main()