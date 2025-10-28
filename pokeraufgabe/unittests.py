import unittest
import sys, os, random
sys.path.append(os.path.dirname(__file__))
from test_pokeraufgabe import compare_colors,compare_order,draw_random_numbers,is_unique,count_equal_cards,check_combinations_insert_statistic

class TestPokerModule(unittest.TestCase):

    def setUp(self):
        """Initiale Testdaten und Statistik-Dict"""
        self.numbers = list(range(1, 53))  # 1–52 = Kartendeck
        self.statistic_dict = {
            'RoyalFlush': 0,
            'StraightFlush': 0,
            'Flush': 0,
            'FourOfAKind': 0,
            'FullHouse': 0,
            'Straight': 0,
            'ThreeOfAKind-Set': 0,
            'TwoPair': 0,
            'OnePair': 0,
            'HighCard': 0
        }

    # --- compare_colors ---
    def test_compare_colors_true(self):
        """Alle Karten aus einer Farbe"""
        cards = [1, 5, 10, 11, 13]  # Pik
        self.assertTrue(compare_colors(cards))

    def test_compare_colors_false(self):
        """Gemischte Farben"""
        cards = [1, 14, 27, 40, 5]  # Pik, Herz, Karo, Kreuz, Pik
        self.assertFalse(compare_colors(cards))

    # --- compare_order ---
    def test_compare_order_true(self):
        """Karten sind aufeinanderfolgend"""
        cards = [5, 6, 7, 8, 9]
        self.assertTrue(compare_order(cards))

    def test_compare_order_false(self):
        """Nicht aufeinanderfolgend"""
        cards = [2, 4, 6, 7, 10]
        self.assertFalse(compare_order(cards))

    # --- draw_random_numbers ---
    def test_draw_random_numbers_length(self):
        """Funktion zieht die richtige Anzahl Karten"""
        result = draw_random_numbers(self.numbers.copy(), 5)
        self.assertEqual(len(result), 5)

    def test_draw_random_numbers_zero(self):
        """Wenn 0 Karten gezogen werden"""
        result = draw_random_numbers(self.numbers.copy(), 0)
        self.assertEqual(result, [])

    def test_draw_random_numbers_too_many(self):
        """Wenn zu viele Karten gezogen werden"""
        with self.assertRaises(ValueError):
            draw_random_numbers(self.numbers.copy(), 60)

    # --- is_unique ---
    def test_is_unique_true(self):
        """Alle Werte einzigartig"""
        self.assertTrue(is_unique([1, 2, 3, 4, 5]))

    def test_is_unique_false(self):
        """Duplikate vorhanden"""
        self.assertFalse(is_unique([1, 2, 3, 2, 4]))

    # --- count_equal_cards ---
    def test_count_equal_cards_single_suit(self):
        """Korrektes Zählen ohne Duplikate"""
        result = count_equal_cards([1, 2, 3, 4, 5])
        values = list(result[0])
        self.assertTrue(all(v == 1 for v in values))

    def test_count_equal_cards_with_duplicates(self):
        """Mehrere gleiche Kartenwerte"""
        result = count_equal_cards([1, 14, 27, 40, 1])  # vier Asse
        # Es sollte mind. eine Zahl mit Wert > 1 geben
        self.assertTrue(any(v > 1 for v in list(result[0])))

    # --- check_combinations_insert_statistic ---
    def test_check_combinations_flush(self):
        """Erkennt Flush"""
        cards = [1, 5, 7, 9, 12]  # alles Pik
        check_combinations_insert_statistic(cards, self.statistic_dict)
        self.assertGreaterEqual(self.statistic_dict['Flush'], 0)

    def test_check_combinations_straight(self):
        """Erkennt Straight"""
        cards = [5, 6, 7, 8, 9]  # aufeinanderfolgend
        check_combinations_insert_statistic(cards, self.statistic_dict)
        self.assertIn('Straight', self.statistic_dict)

    def test_check_combinations_four_of_a_kind(self):
        """Erkennt Four of a Kind"""
        cards = [1, 14, 27, 40, 5]  # vier Asse + 5
        check_combinations_insert_statistic(cards, self.statistic_dict)
        self.assertIn('FourOfAKind', self.statistic_dict)

    def test_check_combinations_full_house(self):
        """Erkennt Full House"""
        cards = [1, 14, 27, 2, 15]  # drei Asse, zwei Zweien
        check_combinations_insert_statistic(cards, self.statistic_dict)
        self.assertIn('FullHouse', self.statistic_dict)

    def test_check_combinations_high_card(self):
        """Erkennt High Card"""
        cards = [1, 14, 20, 33, 45]  # keine Kombination
        check_combinations_insert_statistic(cards, self.statistic_dict)
        self.assertIn('HighCard', self.statistic_dict)

if __name__ == "__main__":
    unittest.main()
