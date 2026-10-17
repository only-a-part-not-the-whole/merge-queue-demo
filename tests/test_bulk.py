import unittest

from shop.bulk import bulk_price


class BulkTest(unittest.TestCase):
    def test_no_discount_below_ten(self):
        self.assertEqual(bulk_price(2, 9), 18.0)

    def test_discount_at_ten(self):
        self.assertEqual(bulk_price(2, 10), 18.0)


if __name__ == "__main__":
    unittest.main()
