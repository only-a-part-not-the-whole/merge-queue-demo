import unittest

from shop.receipt import receipt_line


class ReceiptTest(unittest.TestCase):
    def test_receipt_line(self):
        self.assertEqual(receipt_line("Tea", 2, 2.5), "2 x Tea  £5.00")


if __name__ == "__main__":
    unittest.main()
