import unittest

from shop.checkout import checkout_total


class CheckoutTest(unittest.TestCase):
    def test_checkout_total(self):
        self.assertEqual(checkout_total([40, 60], discount_percent=10), 108.0)


if __name__ == "__main__":
    unittest.main()
