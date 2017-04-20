import Deck
import Player
import Hand
import Points
import Card

TOTAL_CARDS = 8
COUNT_LIMIT = 31
FIFTEEN = 15
DISCARD = 4


class Game(object):
    def __init__(self):
        self.deck = None
        self.player1 = Player.Player("Player 1")
        self.player2 = Player.Player("Player 2")
        self.crib = None
        self.who_crib = -1
        self.counter = 0
        self.top_card = None

    def deal(self):
        self.deck = Deck.Deck()
        if self.who_crib == -1:
            self.cut_deck()
        self.deck.shuffle()
        for i in range(6):
            current_player = self.get_turn()
            other_player = self.get_not_turn()
            new_card = self.deck.pop_card()
            current_player.hand.add_card(new_card)
            new_card = self.deck.pop_card()
            other_player.hand.add_card(new_card)
        self.top_card = self.deck.cut_deck()

    def discard(self):
        print "=============================="
        print "*****DISCARD*****"
        self.crib = Hand.Hand(4)
        og_player = self.get_turn()
        card_count = 0
        while card_count < DISCARD:
            current_player = self.get_turn()
            card_pos = self.get_card_pos(current_player)
            play_card = current_player.hand.get_card(card_pos)
            self.crib.add_card(play_card)
            current_player.hand.remove_card(play_card)
            if card_count == 1:
                self.change_turn()
            card_count += 1
        if og_player is not self.get_turn():
            self.change_turn()

    def count_cards(self):
        print "=============================="
        print "*****COUNT*****"
        player1_cards = list(self.player1.hand.cards)
        player2_cards = list(self.player2.hand.cards)
        played_cards = []
        current_player = self.get_turn()
        while self.player1.hand.get_cards() > 0 \
                or self.player2.hand.get_cards() > 0:
            print "----------------------"
            print "Player 1: %d points" % self.player1.points
            print "Player 2: %d points" % self.player2.points
            print "----------------------"
            card_pos = self.get_card_pos(current_player)
            play_card = current_player.hand.get_card(card_pos)
            card_val = self.get_card_val(play_card)
            while self.is_bust(card_val):
                answer = raw_input("You cannot play this card. Would you like to try again? (y/n)\t")
                if answer == "y":
                    card_pos = self.get_card_pos(current_player)
                    play_card = current_player.hand.get_card(card_pos)
                    card_val = self.get_card_val(play_card)
                elif answer == "n":
                    self.go()
                    play_card = None
                    break
            if play_card is not None:
                current_player.hand.remove_card(play_card)
                self.counter += card_val
                print "Current count: %d" % self.counter
                self.counting(current_player, played_cards, play_card)
                played_cards.append(play_card)
                if self.counter == COUNT_LIMIT:
                    self.reset_count()
                else:
                    self.change_turn()
            current_player = self.get_turn()

        self.counter = 0
        self.get_turn().add_points(1)
        self.player2.hand.add_cards(player2_cards)
        self.player1.hand.add_cards(player1_cards)

    def counting(self, current_player, played_cards, play_card):
        if len(played_cards) > 0 and played_cards[-1].rank == play_card.rank:
            if len(played_cards) > 1 and played_cards[-2].rank == play_card.rank:
                if len(played_cards) > 2 and played_cards[-3].rank == play_card.rank:
                    current_player.add_points(12)
                else:
                    current_player.add_points(6)
            else:
                current_player.add_points(2)

        if self.counter == FIFTEEN:
            current_player.add_points(2)
        if self.counter == COUNT_LIMIT:
            current_player.add_points(2)

    def calculate_points_in_hand(self):
        current_player = self.get_turn()
        crib = self.crib
        other_player = self.get_not_turn()

        print "Calculating points for %s..." % other_player.name
        points = Points.Points(other_player, other_player.hand.cards, self.top_card, False)
        points.run_points()
        print "Calculating points for %s..." % current_player.name
        points = Points.Points(current_player, current_player.hand.cards, self.top_card, True)
        points.run_points()
        print "Calculating points for crib of %s..." % current_player.name
        points = Points.Points(current_player, crib.cards, self.top_card, False)
        points.run_points()

    def cut_deck(self):
        print "=============================="
        print "*****CUT DECK*****"
        card1, card2 = Card.Card(0, 0), Card.Card(0, 0)
        while card1.rank == card2.rank:
            card1 = self.deck.cut_deck()
            card2 = self.deck.cut_deck()
        print "Player 1 gets: %s" % card1
        print "Player 2 gets: %s" % card2
        if card1.rank > card2.rank:
            self.who_crib = 0
            print "Player 1 will start with the crib"
            return self.player1
        else:
            self.who_crib = 1
            print "Player 2 will start with the crib"
            return self.player2

    def go(self):
        self.get_not_turn().add_points(1)
        self.change_turn()
        self.counter = 0

    def reset_count(self):
        self.change_turn()
        self.counter = 0

    def get_card_pos(self, current_player):
        print "=============================="
        print current_player.hand
        print "=============================="
        card_pos = input("%s:\nEnter card index:\t" % current_player.name)
        while card_pos >= current_player.hand.get_cards():
            card_pos = input("Invalid Entry. Please try again:\t")
        return card_pos

    def get_card_val(self, play_card):
        if play_card.rank == 1:
            card_val = int(input("You have chosen an Ace. Would you like to count it as 1 or 11?\t"))
            while not (card_val == 1 or card_val == 11):
                card_val = int(input("Invalid entry. Please choose 1 or 11."))
        else:
            if play_card.rank > 10:
                card_val = 10
            else:
                card_val = play_card.rank
        return card_val

    def is_bust(self, card_val):
        return self.counter + card_val > 31

    def get_turn(self):
        if self.who_crib == 0:
            return self.player1
        else:
            return self.player2

    def get_not_turn(self):
        if self.who_crib == 0:
            return self.player2
        else:
            return self.player1

    def change_turn(self):
        if self.who_crib == 0:
            self.who_crib = 1
        else:
            self.who_crib = 0


if __name__ == '__main__':
    game = Game()
    while game.player1.points < 121 or game.player2.points < 121:
        game.deal()
        game.discard()
        game.count_cards()
        game.calculate_points_in_hand()
        game.player1.hand = Hand.Hand(6)
        game.player2.hand = Hand.Hand(6)
        game.change_turn()

