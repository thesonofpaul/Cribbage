import unittest
import Game
import Points
import Card


class TestPoints(unittest.TestCase):

    def setUp(self):
        self.game = Game.Game()
        self.game.deal()
        self.points1 = Points.Points(self.game.player1, self.game.player1.hand.cards, self.game.top_card, False)
        self.points2 = Points.Points(self.game.player2, self.game.player2.hand.cards, self.game.top_card, True)

    def test_cards_only_rank(self):
        for card in self.points1.cards_only_rank:
            self.assertTrue(0 <= card <= 13)
        for card in self.points2.cards_only_rank:
            self.assertTrue(0 <= card <= 13)

    def test_fifteens(self):
        self.game.player1.points = 0
        fifteens_points = Points.Points(self.game.player1, [Card.Card(0, 1),
                                                            Card.Card(0, 5),
                                                            Card.Card(0, 5),
                                                            Card.Card(0, 10)], Card.Card(0, 10), False)
        fifteens_points.fifteens(0, 0)
        self.assertTrue(self.game.player1.points == 8)

        self.game.player1.points = 0
        fifteens_points = Points.Points(self.game.player1, [Card.Card(0, 11),
                                                            Card.Card(0, 12),
                                                            Card.Card(0, 13),
                                                            Card.Card(0, 5)], Card.Card(0, 10), False)
        fifteens_points.fifteens(0, 0)
        self.assertTrue(self.game.player1.points == 8)

        self.game.player1.points = 0
        fifteens_points = Points.Points(self.game.player1, [Card.Card(0, 8),
                                                            Card.Card(0, 7),
                                                            Card.Card(0, 9),
                                                            Card.Card(0, 6)], Card.Card(0, 10), False)
        fifteens_points.fifteens(0, 0)
        self.assertTrue(self.game.player1.points == 4)

    def test_pairs(self):
        self.game.player1.points = 0
        pairs_points = Points.Points(self.game.player1, [Card.Card(0, 1),
                                                         Card.Card(0, 5),
                                                         Card.Card(1, 5),
                                                         Card.Card(0, 10)], Card.Card(2, 10), False)
        pairs_points.pairs()
        self.assertTrue(self.game.player1.points == 4)

        self.game.player1.points = 0
        pairs_points = Points.Points(self.game.player1, [Card.Card(0, 4),
                                                         Card.Card(0, 4),
                                                         Card.Card(0, 4),
                                                         Card.Card(0, 2)], Card.Card(0, 10), False)
        pairs_points.pairs()
        self.assertTrue(self.game.player1.points == 6)

        self.game.player1.points = 0
        pairs_points = Points.Points(self.game.player1, [Card.Card(0, 10),
                                                         Card.Card(0, 10),
                                                         Card.Card(0, 10),
                                                         Card.Card(0, 10)], Card.Card(0, 1), False)
        pairs_points.pairs()
        self.assertTrue(self.game.player1.points == 12)

    def test_runs(self):
        self.game.player1.points = 0
        pairs_points = Points.Points(self.game.player1, [Card.Card(0, 1),
                                                         Card.Card(0, 1),
                                                         Card.Card(0, 2),
                                                         Card.Card(0, 3)], Card.Card(0, 4), False)
        pairs_points.runs()
        self.assertTrue(self.game.player1.points == 8)

        self.game.player1.points = 0
        pairs_points = Points.Points(self.game.player1, [Card.Card(0, 9),
                                                         Card.Card(0, 10),
                                                         Card.Card(0, 10),
                                                         Card.Card(0, 11)], Card.Card(0, 3), False)
        pairs_points.runs()
        self.assertTrue(self.game.player1.points == 6)

        self.game.player1.points = 0
        pairs_points = Points.Points(self.game.player1, [Card.Card(0, 2),
                                                         Card.Card(0, 3),
                                                         Card.Card(0, 4),
                                                         Card.Card(0, 5)], Card.Card(0, 9), False)
        pairs_points.runs()
        self.assertTrue(self.game.player1.points == 4)

    def test_flush(self):
        self.game.player1.points = 0
        pairs_points = Points.Points(self.game.player1, [Card.Card(0, 2),
                                                         Card.Card(0, 3),
                                                         Card.Card(0, 4),
                                                         Card.Card(0, 5)], Card.Card(1, 9), False)
        pairs_points.flush()
        self.assertTrue(self.game.player1.points == 4)

        self.game.player1.points = 0
        pairs_points = Points.Points(self.game.player1, [Card.Card(2, 2),
                                                         Card.Card(2, 3),
                                                         Card.Card(2, 4),
                                                         Card.Card(2, 5)], Card.Card(2, 9), False)
        pairs_points.flush()
        self.assertTrue(self.game.player1.points == 5)

    def test_nobs(self):
        self.game.player1.points = 0
        pairs_points = Points.Points(self.game.player1, [Card.Card(0, 2),
                                                         Card.Card(1, 11),
                                                         Card.Card(0, 4),
                                                         Card.Card(0, 5)], Card.Card(1, 9), True)
        pairs_points.nobs()
        self.assertTrue(self.game.player1.points == 1)

        self.game.player1.points = 0
        pairs_points = Points.Points(self.game.player1, [Card.Card(0, 2),
                                                         Card.Card(1, 11),
                                                         Card.Card(0, 4),
                                                         Card.Card(2, 11)], Card.Card(2, 9), True)
        pairs_points.nobs()
        self.assertTrue(self.game.player1.points == 1)

        self.game.player1.points = 0
        pairs_points = Points.Points(self.game.player1, [Card.Card(0, 2),
                                                         Card.Card(1, 11),
                                                         Card.Card(0, 4),
                                                         Card.Card(0, 5)], Card.Card(1, 9), False)
        pairs_points.nobs()
        self.assertTrue(self.game.player1.points == 0)
