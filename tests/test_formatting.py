import unittest

from shop.formatting import format_price


class FormattingTest(unittest.TestCase):
    def test_format_price(self):
        self.assertEqual(format_price(1234.5), "£1,234.50")


if __name__ == "__main__":
    unittest.main()
