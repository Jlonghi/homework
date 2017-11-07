import unittest
from PricePackager import pricePackager
class TestPricePackager(unittest.TestCase):

    def testCase1(self):
        self.assertEqual(pricePackager(1299.99, '3 people', 'food'), 1591.58)

    def testCase2(self):
        self.assertEqual(pricePackager(5432.00, '1 person', 'pharmaceutical'), 6199.81)

    def testCase3(self):
        self.assertEqual(pricePackager(12456.95, '4 people', 'books'), 13707.63)
    
    def testCase4(self):
        self.assertEqual(pricePackager(12456.95, '-4 people', 'books'), 13707.63)

    def testCase5(self):
        self.assertEqual(pricePackager(-12456.95, '4 people', 'books'), 13707.63)

if __name__ == '__main__':
    unittest.main()