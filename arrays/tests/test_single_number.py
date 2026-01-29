from arrays.single_number import get_single
from unittest import TestCase


class TestSingleNumber(TestCase):
    def test_get_single_normal_arrays(self):
        array = [1, 1, 2, 2, 2]
        self.assertEqual(get_single(array), 2)

        array = [8, 8, 7, 7, 6, 6, 1]
        self.assertEqual(get_single(array), 1)

        array = [16, 0, 5, 2, 16, 5, 2, 2, 1, 3, 0, 1, 2, 3, 0]
        self.assertEqual(get_single(array), 0)

    def test_one_length_array(self):
        array = [1]
        self.assertEqual(get_single(array), 1)

        array = [0]
        self.assertEqual(get_single(array), 0)

        array = [17]
        self.assertEqual(get_single(array), 17)
