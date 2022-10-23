from doctest import product
from deckofcards import Card, Deck
import unittest2


class Test(unittest2.TestCase):
    def test_product(self):
        self.assertEqual(product(2, 5), 10)


class TestCard(unittest2.TestCase):
    def setUp(self):
        self.cards = Card("Hearts", "A")

    def test_init(self):
        self.assertEqual(self.cards.suit, "Hearts")
        self.assertEqual(self.cards.value, "A")


if __name__ == '__main__':
    unittest2.main()



