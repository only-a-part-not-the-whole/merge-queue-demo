import unittest

from shop.pricing import add_tax, apply_discount


class PricingTest(unittest.TestCase):
    def test_apply_discount(self):
        self.assertEqual(apply_discount(100, 25), 75.0)

    def test_apply_discount_rejects_bad_percent(self):
        with self.assertRaises(ValueError):
            apply_discount(100, 150)

    def test_add_tax(self):
        self.assertEqual(add_tax(100), 120.0)


if __name__ == "__main__":
    unittest.main()
