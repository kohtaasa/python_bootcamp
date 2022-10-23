import doctest
import unittest2

class Test(unittest2.TestCase):
    def test_product(self):
        self.assartEqual(self.product(2, 5), 10)


