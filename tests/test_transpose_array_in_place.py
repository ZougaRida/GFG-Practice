import unittest
from random import shuffle
from transpose_array_in_place import method2, method1


class TestMethod2(unittest.TestCase):
    """
    This class makes sure to test all different cases for method 2.
    Of course, again the array elements are from 0 to n - 1 where n is the length of array.
    """

    def test_valid_rearrangement(self):
        arr = [4, 0, 2, 1, 3]
        method2(arr, len(arr))
        self.assertEqual(arr, [3, 4, 2, 0, 1])

        arr = [3, 2, 0, 1]
        method2(arr, len(arr))
        self.assertEqual(arr, [1, 0, 3, 2])

        arr = [1, 0]
        method2(arr, len(arr))
        self.assertEqual(arr, [0, 1])

    def test_single_element_array(self):
        arr = [0]
        method2(arr, len(arr))
        self.assertEqual(arr, [0])

    def test_already_rearranged(self):
        # Honestly, this case could have been included in the first method.
        # though since it's special such that the array doesn't change after passing it to the method,
        # I decided to include it as a special case.
        arr = list(range(10))
        method2(arr, len(arr))
        self.assertEqual(arr, arr)


class TestMethod1(unittest.TestCase):
    def test_method1_gives_same_output_as_method2(self):
        """This one makes sure that method1 and 2 are basically the same in terms of output."""
        arr1 = [5, 2, 0, 3, 4, 1]
        arr2 = arr1.copy()
        method1(arr1, len(arr1))
        method2(arr2, len(arr2))
        self.assertListEqual(arr1, arr2)

        arr1 = list(range(20))
        shuffle(arr1)
        arr2 = arr1.copy()
        method1(arr1, len(arr1))
        method2(arr2, len(arr2))
        self.assertListEqual(arr1, arr2)


# if __name__ == "__main__":
#     unittest.main()
