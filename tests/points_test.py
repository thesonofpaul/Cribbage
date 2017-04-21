import unittest
import Game
import Points
import Card
import Player


class TestPoints(unittest.TestCase):
    def test_cards_only_rank(self):
        test_player1 = Player.Player("Player 1", False)
        test_player2 = Player.Player("Player 2", False)
        self.game = Game.Game(test_player1, test_player2)
        self.game.deal()
        self.game.top_card = self.game.deck.cut_deck()
        self.points1 = Points.Points(self.game.player1.hand.cards, self.game.top_card)
        self.points2 = Points.Points(self.game.player2.hand.cards, self.game.top_card)
        for card in self.points1.cards_only_rank:
            self.assertTrue(0 <= card <= 13)
        for card in self.points2.cards_only_rank:
            self.assertTrue(0 <= card <= 13)

    def test_fifteens(self):
        fifteens_points = Points.Points([Card.Card(0, 1),
                                         Card.Card(0, 5),
                                         Card.Card(0, 5),
                                         Card.Card(0, 10)], Card.Card(0, 10))
        fifteens_points.fifteens(0, 0)
        self.assertTrue(fifteens_points.points == 8)

        fifteens_points = Points.Points([Card.Card(0, 11),
                                         Card.Card(0, 12),
                                         Card.Card(0, 13),
                                         Card.Card(0, 5)], Card.Card(0, 10))
        fifteens_points.fifteens(0, 0)
        self.assertTrue(fifteens_points.points == 8)

        fifteens_points = Points.Points([Card.Card(0, 8),
                                         Card.Card(0, 7),
                                         Card.Card(0, 9),
                                         Card.Card(0, 6)], Card.Card(0, 10))
        fifteens_points.fifteens(0, 0)
        self.assertTrue(fifteens_points.points == 4)

    def test_pairs(self):
        pairs_points = Points.Points([Card.Card(0, 1),
                                      Card.Card(0, 5),
                                      Card.Card(1, 5),
                                      Card.Card(0, 10)], Card.Card(2, 10))
        pairs_points.pairs()
        self.assertTrue(pairs_points.points == 4)

        pairs_points = Points.Points([Card.Card(0, 13),
                                      Card.Card(0, 13),
                                      Card.Card(0, 13),
                                      Card.Card(0, 2)], Card.Card(0, 10))
        pairs_points.pairs()
        self.assertTrue(pairs_points.points == 6)

        pairs_points = Points.Points([Card.Card(0, 10),
                                      Card.Card(0, 10),
                                      Card.Card(0, 10),
                                      Card.Card(0, 10)], Card.Card(0, 1))
        pairs_points.pairs()
        self.assertTrue(pairs_points.points == 12)

    def test_runs(self):
        run_points = Points.Points([Card.Card(0, 1),
                                    Card.Card(0, 1),
                                    Card.Card(0, 2),
                                    Card.Card(0, 3)], Card.Card(0, 4))
        run_points.runs()
        self.assertTrue(run_points.points == 8)

        run_points = Points.Points([Card.Card(0, 9),
                                    Card.Card(0, 10),
                                    Card.Card(0, 10),
                                    Card.Card(0, 11)], Card.Card(0, 3))
        run_points.runs()
        self.assertTrue(run_points.points == 6)

        run_points = Points.Points([Card.Card(0, 2),
                                    Card.Card(0, 3),
                                    Card.Card(0, 4),
                                    Card.Card(0, 5)], Card.Card(0, 9))
        run_points.runs()
        self.assertTrue(run_points.points == 4)

    def test_flush(self):
        flush_points = Points.Points([Card.Card(0, 2),
                                      Card.Card(0, 3),
                                      Card.Card(0, 4),
                                      Card.Card(0, 5)], Card.Card(1, 9))
        flush_points.flush()
        self.assertTrue(flush_points.points == 4)

        flush_points = Points.Points([Card.Card(2, 2),
                                      Card.Card(2, 3),
                                      Card.Card(2, 4),
                                      Card.Card(2, 5)], Card.Card(2, 9))
        flush_points.flush()
        self.assertTrue(flush_points.points == 5)

    def test_nobs(self):
        nobs_points = Points.Points([Card.Card(0, 2),
                                     Card.Card(1, 11),
                                     Card.Card(0, 4),
                                     Card.Card(0, 5)], Card.Card(1, 9))
        nobs_points.nobs()
        self.assertTrue(nobs_points.points == 1)

        nobs_points = Points.Points([Card.Card(0, 2),
                                     Card.Card(1, 11),
                                     Card.Card(0, 4),
                                     Card.Card(2, 11)], Card.Card(2, 9))
        nobs_points.nobs()
        self.assertTrue(nobs_points.points == 1)

        nobs_points = Points.Points([Card.Card(0, 2),
                                     Card.Card(2, 11),
                                     Card.Card(0, 4),
                                     Card.Card(0, 5)], Card.Card(2, 9))
        nobs_points.nobs()
        self.assertTrue(nobs_points.points == 1)
