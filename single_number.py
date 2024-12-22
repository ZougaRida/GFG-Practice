def get_single(arr):
    """
    Compute the element that appears only once in the given array
    while all other elements appear an even number of times.

    This function uses the XOR operation to identify the unique
    element with time complexity O(n) and space complexity O(1)
    which definitley is the most efficient out of all other ways.

    :param arr: The list of positive integers.
    :type arr: list[int]
    :return: The single integer that appears only once in the array.
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