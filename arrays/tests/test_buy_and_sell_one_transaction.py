from unittest import TestCase

from buy_and_sell_one_transaction import maximum_profit


class TestTransaction(TestCase):
    def test_normal_length_array(self):
        array = [7, 10, 1, 3, 6, 9, 2]
        self.assertEqual(maximum_profit(array), 8)

        array = [7, 6, 4, 3, 1]
        self.assertEqual(maximum_profit(array), 0)

        array = [7, 6, 4, 3, 1, 1000]
        self.assertEqual(maximum_profit(array), 999)

        array = list(range(100))
        self.assertEqual(maximum_profit(array), 99)

    def test_length_one_array(self):
        array = [1]
        self.assertEqual(maximum_profit(array), 0)

        array = [32]
        self.assertEqual(maximum_profit(array), 0)
