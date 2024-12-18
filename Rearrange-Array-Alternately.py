def rearrange(arr):
    """
    Rearranges an input array `arr` such that the modified array contains alternating
    maximum and minimum elements from the original sorted array. The operation is
    performed in-place to optimize space usage.

    This algorithm uses the concept of encoding two numbers into one index to
    avoid using extra space for the rearrangement. The original array is first
    sorted, and then the maximum and minimum values are interleaved using modular
    arithmetic.

    :param arr: A list of integers. The array to be rearranged in-place. The input
        list will be modified as a result of this operation.
    :type arr: list[int]

    :return: None. The function modifies the input array `arr` directly.


    The upper documentation was generated with AI which is pretty good.
    Always remember the powerful way of encoding 2 values in one position using modular arithmetic.
    https://www.geeksforgeeks.org/problems/-rearrange-array-alternately-1587115620/1

    """

    arr.sort()

    n = len(arr)

    left, right = 0, n - 1
    max_value = arr[-1] + 1
    flag = True

    for i in range(n):
        if flag:
            arr[i] += (arr[right] % max_value) * max_value
            right -= 1
            flag = False
        else:
            arr[i] += (arr[left] % max_value) * max_value
            left += 1
            flag = True

    for i in range(n):
        arr[i] //= max_value



array = [int(x) for x in input().split()]
rearrange(array)
print(array)