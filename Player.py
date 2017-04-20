import Hand

POINTS_TO_WIN = 121


class Player(object):

    def __init__(self, name):
        self.name = name
        self.hand = Hand.Hand(6)
        self.points = 0

    def add_points(self, num):
        self.points += num
        print "%s awarded %d points, bringing the total to %d" % \
              (self.name, num, self.points)

    def is_win(self):
        return self.points >= POINTS_TO_WIN

    def reset(self):
        self.points = 0
        self.hand.clear()
