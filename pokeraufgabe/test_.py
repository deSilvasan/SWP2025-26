import unittest
from pokeraufgabe.pokeraufgabe import (fill_array_numbers, compare_colors, compare_order, draw_random_numbers, is_unique,
                          count_equal_cards, check_combinations_insert_statistic)

class MyTestCase(unittest.TestCase):
    def test_fill_array_numbers(self):
        self.assertEqual(fill_array_numbers(0), [])
        self.assertEqual(fill_array_numbers(1), [0])
        self.assertEqual(fill_array_numbers(5), [0, 1, 2, 3, 4])

    def test_compare_colors(self):
        # all cards same suit (♠, hearts, clubs)
        self.assertTrue(compare_colors([0, 1, 2, 3]))
        self.assertTrue(compare_colors([13, 14, 15]))
        self.assertFalse(compare_colors([0, 13]))
        self.assertFalse(compare_colors([0, 26, 39]))

    def test_compare_order(self):
        # colorImportant True checks in simple sorted order
        self.assertTrue(compare_order([0, 1, 2, 3, 4], True))
        self.assertFalse(compare_order([0, 2, 3, 4, 5], True))
        # colorImportant False checks modulo 13 values sorted
        self.assertFalse(compare_order([0, 13, 26, 39], False))  # all 0 mod 13, is consecutive by modulo?
        self.assertTrue(compare_order([7, 8, 9, 10], True))
        self.assertFalse(compare_order([7, 8, 10, 11], True))

    def test_draw_random_numbers(self):
        numbers = fill_array_numbers(10)
        random_draw = draw_random_numbers(numbers, 5)
        self.assertEqual(len(random_draw), 5)
        self.assertTrue(all(n in range(10) for n in random_draw))

    def test_is_unique(self):
        self.assertTrue(is_unique([0, 1, 2, 3]))
        self.assertFalse(is_unique([0, 1, 1, 2]))

    def test_count_equal_cards(self):
        # All four suits of rank 2 (index 0 mod 13)
        self.assertEqual(sorted(count_equal_cards([0, 13, 26, 39])), [4])
        # 3 cards of rank 2, 2 cards of rank 3
        test_cards = [0, 13, 26, 1, 14]
        self.assertCountEqual(count_equal_cards(test_cards), [3, 2])

    def test_check_combinations_insert_statistic(self):
        stat = {k: 0 for k in
                ['HighCard', 'OnePair', 'TwoPair', 'ThreeOfAKind-Set', 'Straight', 'Flush', 'FullHouse', 'FourOfAKind',
                 'StraightFlush', 'RoyalFlush']}
        # Royal Flush example (♠ 10, J, Q, K, A = 8,9,10,11,12)
        royal_flush = [8, 9, 10, 11, 12]
        check_combinations_insert_statistic(royal_flush, stat)
        self.assertEqual(stat['RoyalFlush'], 1)

        stat = {k: 0 for k in stat}
        # Four of a Kind: four 2's + one different card
        four_kind = [0, 13, 26, 39, 11]
        check_combinations_insert_statistic(four_kind, stat)
        self.assertEqual(stat['FourOfAKind'], 1)

        stat = {k: 0 for k in stat}
        # Full House: three 2's and two 3's
        full_house = [0, 13, 1, 14, 26]
        check_combinations_insert_statistic(full_house, stat)
        self.assertEqual(stat['FullHouse'], 1)

        stat = {k: 0 for k in stat}
        # Flush: five cards same suit no order
        flush = [0, 4, 5, 6, 8]
        check_combinations_insert_statistic(flush, stat)
        self.assertEqual(stat['Flush'], 1)

        stat = {k: 0 for k in stat}
        # Straight: five consecutive cards, mixed suits
        straight = [1, 15, 29, 43, 44]
        check_combinations_insert_statistic(straight, stat)
        print(stat)
        self.assertEqual(stat['Straight'], 1)

        stat = {k: 0 for k in stat}
        # One Pair: two cards of same rank
        one_pair = [0, 13, 2, 3, 4]
        check_combinations_insert_statistic(one_pair, stat)
        self.assertEqual(stat['OnePair'], 1)

        stat = {k: 0 for k in stat}
        # High Card: no pair, no sequence
        high_card = [0, 5, 10, 20, 27]
        check_combinations_insert_statistic(high_card, stat)
        self.assertEqual(stat['HighCard'], 1)


if __name__ == '__main__':
    unittest.main()
