from doctest import product
import unittest2


class Test(unittest2.TestCase):
    def test_product(self):
        self.assartEqual(product(2, 5), 10)


if __name__ == '__main__':
    unittest2.main()



