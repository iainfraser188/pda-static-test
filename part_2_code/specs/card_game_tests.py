import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    def setUp(self):
        self.card_game = CardGame()
        self.card1 = Card("clubs",4)
        self.card2 = Card("spades",1) 
    
    
    def test_check_for_ace_true(self):
        self.assertEqual(True,self.card_game.check_for_ace(self.card2))
    
    def test_check_for_ace_false(self):
        self.assertEqual(False,self.card_game.check_for_ace(self.card1))
    
    def test_highest_card(self):
        self.assertEqual(self.card1, self.card_game.highest_card(self.card1,self.card2))

    def test_cards_total(self) :
        cards = [self.card1,self.card2]
        self.assertEqual("You have a total of 5",self.card_game.cards_total(cards))