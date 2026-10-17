import unittest

from shop.shipping import shipping_cost


class ShippingTest(unittest.TestCase):
    def test_free_over_threshold(self):
        self.assertEqual(shipping_cost(50), 0.0)

    def test_flat_rate_below_threshold(self):
        self.assertEqual(shipping_cost(49.99), 4.99)


if __name__ == "__main__":
    unittest.main()
