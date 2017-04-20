

class Points(object):

    def __init__(self, current_player, cards, top_card, is_crib):
        self.cards = cards
        self.cards.append(top_card)
        self.cards_only_rank = []
        for card in self.cards:
            self.cards_only_rank.append(card.rank)
        self.cards_only_rank.sort()
        self.top_card = top_card
        self.is_crib = is_crib
        self.player = current_player

    def run_points(self):
        print "---------------"
        for card in self.cards:
            print card
        print "---------------"

        self.fifteens(0, 0)
        self.pairs()
        self.runs()
        self.flush()
        self.nobs()

    def fifteens(self, index, total):
        print "fifteens"
        for i in range(index, 5):
            value = 10 if self.cards_only_rank[i] > 9 else self.cards_only_rank[i]
            subtotal = total + value
            if subtotal == 15:
                self.player.add_points(2)
            elif subtotal < 15:
                self.fifteens(i + 1, subtotal)

    def pairs(self):
        print "pairs"
        for i in range(len(self.cards_only_rank)):
            for j in range(len(self.cards_only_rank)):
                if j > i and self.cards_only_rank[i] == self.cards_only_rank[j]:
                    self.player.add_points(2)

    def runs(self):
        print "runs"
        for index in range(len(self.cards_only_rank)-2):
            card1 = self.cards_only_rank[index]
            card2 = self.cards_only_rank[index+1]
            card3 = self.cards_only_rank[index+2]
            card4 = None
            card5 = None
            if index < len(self.cards_only_rank)-3:
                card4 = self.cards_only_rank[index+3]
            if index < len(self.cards_only_rank) - 4:
                card5 = self.cards_only_rank[index+4]

            if card1+1 == card2 and card2+1 == card3:
                if card3+1 == card4:
                    if card4+1 == card5:
                        self.player.add_points(5)
                    elif card4 == card5:
                        self.player.add_points(8)
                    else:
                        self.player.add_points(4)
                    break
                elif card3 == card4:
                    if card4 == card5:
                        self.player.add_points(9)
                    elif card4+1 == card5:
                        self.player.add_points(8)
                    else:
                        self.player.add_points(6)
                    break
                else:
                    self.player.add_points(3)
            elif card1+1 == card2 and card2 == card3:
                if card3 == card4 and card4+1 == card5:
                    self.player.add_points(9)
                elif card3+1 == card4:
                    if card4 == card5:
                        self.player.add_points(12)
                    elif card4+1 == card5:
                        self.player.add_points(8)
                    else:
                        self.player.add_points(6)
                    break
            elif card1 == card2 and card2+1 == card3:
                if card3 == card4 and card4+1 == card5:
                    self.player.add_points(12)
                elif card3+1 == card4:
                    if card4 == card5:
                        self.player.add_points(12)
                    elif card4+1 == card5:
                        self.player.add_points(8)
                    else:
                        self.player.add_points(6)
                break
            elif card1 == card2 == card3 and card3+1 == card4 and card4+1 == card5:
                self.player.add_points(9)
                break

    def flush(self):
        print "flush"
        temp_cards = self.cards
        temp_cards.remove(self.top_card)
        for i in range(len(temp_cards)-1):
            if temp_cards[i].suit != temp_cards[i+1].suit:
                return
        if temp_cards[0].suit == self.top_card.suit:
            self.player.add_points(5)
        else:
            self.player.add_points(4)

    def nobs(self):
        print "nobs"
        if self.top_card.rank == 11:
            self.player.add_points(1)
            return
        if self.is_crib:
            for card in self.cards:
                if card.rank == 11 and card.suit == self.top_card.suit:
                    self.player.add_points(1)

