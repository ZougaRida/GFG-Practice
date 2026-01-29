from typing import Annotated
from annotated_types import Gt

type positive_int = Annotated[int, Gt(0)]


def rearrange(arr: list[positive_int]) -> None:
    """
    Rearranges an input array `arr` such that the modified array contains alternating
    maximum and minimum elements from the original sorted array. The operation is
    performed in-place to optimize space usage.

    This algorithm uses the concept of encoding two numbers into one index to
    avoid using extra space for the rearrangement. The original array is first
    sorted, and then the maximum and minimum values are interleaved using modular
    arithmetic.

    The upper documentation was generated with AI which is pretty good.
    **Always remember the powerful way of encoding 2 values in one position using
    modular arithmetic.**

    https://www.geeksforgeeks.org/problems/-rearrange-array-alternately-1587115620/1

    :param list[int] arr: A list of integers. The array to be rearranged in-place. The
           input list will be modified as a result of this operation.

    :return: None. The function modifies the input array `arr` in-place.

    """
    # of course, we need to sort first the array before doing anything
    # to know the consecutive mins and maxs
    arr.sort()

    n = len(arr)

    # left keep track of mins
    # right keep track of maxs
    left, right = 0, n - 1

    # after sorting, arr[-1] is max of array, thus encoder = arr[-1] + 1 is
    # guaranteed to be strictly greater than all the elements of arr
    encoder = arr[-1] + 1

    for i in range(n):
        # for even indexes they should contain maxs
        # for odd indexes they should contain mins
        if i % 2 == 0:
            arr[i] += (arr[right] % encoder) * encoder
            right -= 1
        else:
            arr[i] += (arr[left] % encoder) * encoder
            left += 1

    # now we clean the array
    # since all values are of the form: encoder * q + remainder
    # where 0 < remainder < encoder
    # and we want to keep only the remainder in each index
    for i in range(n):
        arr[i] //= encoder


if __name__ == "__main__":
    array = [int(x) for x in input().split()]
    rearrange(array)
    print(array)
