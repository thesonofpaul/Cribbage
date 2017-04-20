import unittest
import Game


class TestCount(unittest.TestCase):

    def setUp(self):
        self.game = Game.Game()

    def test_deal(self):
        self.game.deal()
        self.assertTrue(self.game.player1.hand.get_cards() == 6)
        self.assertTrue(self.game.player2.hand.get_cards() == 6)

    # def test_discard(self):
    #     self.game.discard()
    #     self.assertTrue(len(self.game.crib) == 4)

    # def test_count_cards(self):
    #     self.game.count_cards()
