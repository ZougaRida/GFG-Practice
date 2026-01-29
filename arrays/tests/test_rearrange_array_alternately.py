from unittest import TestCase
from arrays.rearrange_array_alternately import rearrange


class TestRearrangeMethod(TestCase):
    # Remember that array is modified in place
    def test_normal_arrays(self):
        array = [1, 2, 3, 4, 5, 6]
        rearrange(array)
        self.assertEqual(array, [6, 1, 5, 2, 4, 3])

        array = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110]
        rearrange(array)
        self.assertEqual(array, [110, 10, 100, 20, 90, 30, 80, 40, 70, 50, 60])

        array = [16, 1]
        rearrange(array)
        self.assertEqual(array, [16, 1])

    def test_one_length_array(self):
        array = [1]
        rearrange(array)
        self.assertEqual(array, [1])

        array = [23]
        rearrange(array)
        self.assertEqual(array, [23])
