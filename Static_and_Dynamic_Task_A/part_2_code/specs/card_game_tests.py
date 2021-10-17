import unittest
from src.card import Card
from src.card_game import CardGame


class TestCardGame(unittest.TestCase):

    def setUp(self):
        self.card1 = Card("Hearts", 10)
        self.card2 = Card("Spades", 12)
        self.game = CardGame()
        self.cards = [self.card1, self.card2]

    def test_check_for_ace(self):
        self.assertEqual(False, self.game.check_for_ace(self.card1))

    def test_returns_highest_card(self):
        self.assertEqual(self.card2, self.game.highest_card(self.card1, self.card2))

    def test_returns_cards_total(self):
        self.assertEqual("You have a total of 22", self.game.cards_total(self.cards))