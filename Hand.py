import Card


class Hand(object):

    def __init__(self, limit):
        self.cards = []
        self.limit = limit

    def __str__(self):
        i = 0
        res = []
        for card in self.cards:
            res.append("%d: %s" % (i, str(card)))
            i += 1
        return '\n'.join(res)

    def add_card(self, card):
        if len(self.cards) < self.limit:
            self.cards.append(card)
            return self.get_cards()
        else:
            print "Hand is full. Cannot add card %s" % card

    def add_cards(self, cards):
        for item in cards:
            if len(self.cards) < self.limit:
                self.cards.append(item)
            else:
                print "Hand is full. Cannot add card %s" % item
        return self.cards

    def remove_card(self, card):
        self.cards.remove(card)
        return self.get_cards()

    def clear(self):
        self.cards = []

    def get_cards(self):
        return len(self.cards)

    def get_card(self, index):
        return self.cards[index]
