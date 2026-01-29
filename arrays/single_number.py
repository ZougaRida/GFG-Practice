from typing import Annotated
from annotated_types import Gt

type positive_int = Annotated[int, Gt(-1)]


def get_single(arr: list[positive_int]) -> positive_int:
    """
    Compute the element that appears an odd number of times in the given array
    while all other elements appear an even number of times.

    This function uses the `XOR` operation to identify the unique
    element with time complexity `O(n)` and space complexity `O(1)`
    which definitely is the most efficient out of all other ways.

    :math:`a \\operatorname{XOR} a = 0` and :math:`a \\operatorname{XOR} 0 = a`

    https://www.geeksforgeeks.org/problems/single-number1014/1

    :param list[int] arr: The list of positive integers.
    :return: The single integer that appears an odd number of times in the array.
    :rtype: int
    """
    single = 0
    for num in arr:
        # XOR is a powerful binary operation
        # since 0 XOR a = a and a XOR a = 0
        single ^= num

    return single


if __name__ == "__main__":
    array = [int(x) for x in input().split()]
    result = get_single(array)
    print(result)
