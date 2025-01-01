from unittest import TestCase

from missing_element_of_AP import find_missing


class TestMissingElementOfAP(TestCase):
    def test_missing_middle(self):
        arr = [2, 4, 8, 10]
        self.assertEqual(find_missing(arr), 6)

        arr = [10, 40, 70, 100, 160]
        self.assertEqual(find_missing(arr), 130)

        arr = [1, 6, 11, 16, 21, 31]
        self.assertEqual(find_missing(arr), 26)

        arr = list(range(2, 1000, 2))
        arr.remove(500)
        self.assertEqual(find_missing(arr), 500)

    def test_for_array_length_2(self):
        arr = [1, 3]
        self.assertEqual(find_missing(arr), 2)

        arr = [15, 25]
        self.assertEqual(find_missing(arr), 20)

        arr = [107, 275]
        self.assertEqual(find_missing(arr), 191)
