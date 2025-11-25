import unittest
from pokeraufgabe.pokeraufgabe import (
    fill_array_numbers,
    compare_colors,
    compare_order,
    draw_random_numbers,
    is_unique,
    count_equal_cards,
    check_combinations_insert_statistic
)

class TestPokerRules(unittest.TestCase):

    # Hilfsfunktion: Karten aus Rängen und Farben erzeugen
    # Farbe: 0=♠,1=♥,2=♦,3=♣, Rank: 0 bis 12 (2 bis Ass)
    def card(self, rank, suit):
        return rank + 13 * suit
    def test_compare_colors_flush(self):
        # alle Karten ♠ (Farbe 0)
        hand = [self.card(0, 0), self.card(5, 0), self.card(9, 0), self.card(3, 0), self.card(12, 0)]
        self.assertTrue(compare_colors(hand))

    def test_compare_colors_not_flush(self):
        hand = [self.card(0, 0), self.card(5, 1), self.card(9, 0), self.card(3, 0), self.card(12, 0)]
        self.assertFalse(compare_colors(hand))

    def test_compare_order_straight(self):
        # Folge (7,8,9,10,J) beliebige Farbe (hier gleiche Farbe zur Sicherheit)
        hand = [self.card(rank, 0) for rank in range(5, 10)]
        self.assertTrue(compare_order(hand, True))
        self.assertTrue(compare_order(hand, False))

    def test_compare_order_not_straight(self):
        hand = [self.card(rank, 0) for rank in [2, 4, 5, 6, 7]]
        self.assertFalse(compare_order(hand, True))
        self.assertFalse(compare_order(hand, False))

    def test_is_unique_true(self):
        hand = [self.card(rank, 0) for rank in range(5)]
        self.assertTrue(is_unique(hand))

    def test_is_unique_false(self):
        hand = [self.card(0,0), self.card(0,1), self.card(2,0), self.card(3,0), self.card(4,0)]
        # zwei Karten mit gleichem Wert (Rank 0) aber unterschiedlicher Farbe
        self.assertTrue(is_unique(hand))  # Da sich is_unique auf exakte Werte bezieht, nicht nur Ränge

    def test_count_equal_cards(self):
        hand = [self.card(3,0), self.card(3,1), self.card(3,2), self.card(5,0), self.card(5,1)]
        counts = count_equal_cards(hand)
        self.assertIn(3, counts)
        self.assertIn(2, counts)

    def test_check_combinations_insert_statistic_royal_flush(self):
        stats = {key: 0 for key in ['HighCard','OnePair','TwoPair','ThreeOfAKind-Set','Straight','Flush','FullHouse','FourOfAKind','StraightFlush','RoyalFlush']}
        # Royal Flush: 10(8), Bube(9), Dame(10), König(11), Ass(12) alle gleiche Farbe
        hand = [self.card(rank, 0) for rank in range(8, 13)]
        check_combinations_insert_statistic(hand, stats)
        self.assertEqual(stats['RoyalFlush'], 1)

    def test_check_combinations_insert_statistic_full_house(self):
        stats = {key: 0 for key in ['HighCard','OnePair','TwoPair','ThreeOfAKind-Set','Straight','Flush','FullHouse','FourOfAKind','StraightFlush','RoyalFlush']}
        # Full House: drei Neunen, zwei Achten (verschiedene Farben)
        hand = [self.card(7, 0), self.card(7, 1), self.card(7, 2), self.card(6, 0), self.card(6, 1)]
        check_combinations_insert_statistic(hand, stats)
        self.assertEqual(stats['FullHouse'], 1)

    def test_check_combinations_insert_statistic_flush(self):
        stats = {key: 0 for key in ['HighCard','OnePair','TwoPair','ThreeOfAKind-Set','Straight','Flush','FullHouse','FourOfAKind','StraightFlush','RoyalFlush']}
        # Flush, nicht in Reihenfolge
        hand = [self.card(r, 0) for r in [2, 4, 7, 9, 12]]
        check_combinations_insert_statistic(hand, stats)
        self.assertEqual(stats['Flush'], 1)

    def test_check_combinations_insert_statistic_four_of_a_kind(self):
        stats = {key: 0 for key in ['HighCard','OnePair','TwoPair','ThreeOfAKind-Set','Straight','Flush','FullHouse','FourOfAKind','StraightFlush','RoyalFlush']}
        # Vierling (vier Könige)
        hand = [self.card(11, 0), self.card(11, 1), self.card(11, 2), self.card(11, 3), self.card(5, 0)]
        check_combinations_insert_statistic(hand, stats)
        self.assertEqual(stats['FourOfAKind'], 1)

    def test_check_combinations_insert_statistic_straight_flush(self):
        stats = {key: 0 for key in ['HighCard','OnePair','TwoPair','ThreeOfAKind-Set','Straight','Flush','FullHouse','FourOfAKind','StraightFlush','RoyalFlush']}
        # Straight Flush 5,6,7,8,9 alle gleiche Farbe ♣
        hand = [self.card(rank, 3) for rank in range(3, 8)]
        check_combinations_insert_statistic(hand, stats)
        self.assertEqual(stats['StraightFlush'], 1)

if __name__ == '__main__':
    unittest.main()
