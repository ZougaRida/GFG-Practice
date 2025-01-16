import unittest

from find_extra_element import find_extra_element


class TestFindExtraElement(unittest.TestCase):
    """
    The conditions given in the problem were actually not necessary.

    For example, the array does not need to be sorted in order to work, but though elements
    should be unique though otherwise the algorithm will fail.
    """

    def test_normal_array_conditions(self):
        array = [16, 15, 21]
        array2 = array.copy()
        del array2[1]
        self.assertEqual(15, find_extra_element(array, array2))

        array = [2, 12, 56, 18, 29, 10, 22]
        array2 = array.copy()
        del array2[4]
        self.assertEqual(29, find_extra_element(array, array2))

        array = list(range(20))
        array2 = array.copy()
        del array2[17]
        self.assertEqual(17, find_extra_element(array, array2))

    def test_last_element_deleted(self):
        array = [16, 15, 21]
        array2 = array.copy()
        array2.pop()
        self.assertEqual(21, find_extra_element(array, array2))

        array = [3, 5, 7, 8, 11, 13]
        array2 = array.copy()
        array2.pop()
        self.assertEqual(13, find_extra_element(array, array2))

    def test_first_element_deleted(self):
        array = [16, 15, 21]
        array2 = array.copy()
        del array2[0]
        self.assertEqual(16, find_extra_element(array, array2))

        array = [53, 5]
        array2 = array.copy()
        del array2[0]
        self.assertEqual(53, find_extra_element(array, array2))

        array = list(range(1, 13, 2))
        array2 = array.copy()
        del array2[0]
        self.assertEqual(1, find_extra_element(array, array2))

    def test_length_one_array(self):
        array = [16]
        array2 = array.copy()
        array2.pop()
        self.assertEqual(16, find_extra_element(array, array2))

        array = [-15]
        array2 = []
        self.assertEqual(-15, find_extra_element(array, array2))
