import unittest
import Game
import Player


class TestCount(unittest.TestCase):

    def setUp(self):
        test_player1 = Player.Player("Player 1", False)
        test_player2 = Player.Player("Player 2", False)
        self.game = Game.Game(test_player1, test_player2)

    def test_deal(self):
        self.game.deal()
        self.assertTrue(self.game.player1.hand.get_cards() == 6)
        self.assertTrue(self.game.player2.hand.get_cards() == 6)

    # def test_discard(self):
    #     self.game.discard()
    #     self.assertTrue(len(self.game.crib) == 4)

    # def test_count_cards(self):
    #     self.game.count_cards()
