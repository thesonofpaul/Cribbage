import itertools
import copy
import Hand
import Deck
import Points


def discard(cards, is_crib):

    deck = Deck.Deck()
    for card in cards.cards:
        deck.remove_card(card)

    results_list = []

    for discards in itertools.combinations(cards.cards, 2):

        discard_result = discards
        hand_result = 0
        crib_result = 0

        hand = copy.deepcopy(cards)
        hand.remove_card(discards[0])
        hand.remove_card(discards[1])

        crib = Hand.Hand(4)
        crib.add_cards(discards)

        for top_card in deck.cards:

            deck_copy = copy.deepcopy(deck)
            deck_copy.remove_card(top_card)

            hand_points = Points.Points(hand.cards, top_card)
            hand_points.run_points()
            hand_result += hand_points.points

            count = 0
            for other_discards in itertools.combinations(deck_copy.cards, 2):

                crib_copy = copy.deepcopy(crib)
                crib_copy.add_cards(other_discards)

                crib_points = Points.Points(hand.cards, top_card)
                crib_points.run_points()
                crib_result += crib_points.points

                count += 1

            crib_result /= count

        hand_result /= len(deck.cards)
        crib_result /= len(deck.cards)
        total = hand_result

        if is_crib:
            total += crib_result
        else:
            total -= crib_result

        results_list.append((discard_result, total))

    max_total = -1
    best_discards = None
    for (discards, total) in results_list:
        if total > max_total:
            best_discards = discards
            max_total = total

    print "*****AGENT DISCARDS*****"
    for card in best_discards:
        print card
    print "************************"
    return best_discards


def count_cards(hand, played_cards, current_score):

    possible_hand = []

    for card in hand.cards:
        if card.rank + current_score <= 31:
            possible_hand.append(card)

    if len(possible_hand) == 0:
        return None

    result_list = []

    for card in possible_hand:
        score = 0

        if current_score + card.rank == 15:
            score += 2

        pair_count = 0
        for played in reversed(played_cards):
            if played.rank != played.rank:
                break
            else:
                pair_count += 1
        score += (pair_count * (pair_count+1))

        run_list = []
        for played in reversed(played_cards):
            if abs(card.rank - played.rank) == 1:
                run_list.append(played.rank)
            else:
                for item in run_list:
                    if abs(item - played.rank) == 1 and \
                                    played.rank not in run_list and \
                                    played.rank != card.rank:
                        run_list.append(played.rank)
        score += len(run_list)
        result_list.append((card, score))

    max_score = -1
    best_card = None
    for (card, score) in result_list:
        if score > max_score:
            best_card = card
            max_score = score
    print "*****AGENT COUNT CARD*****"
    print best_card
    print "**************************"
    return best_card
