def transition_point(arr: list[int]) -> int:
    """
    Finds and returns the transition point in a binary sorted array where the first occurrence of
    `1` appears, indicating the start of ones in the array. The function performs a binary search
    to efficiently locate the transition point.

    :param arr: A binary sorted list containing only `0`s followed by `1`s, with a possible single or no transition point
                from `0` to `1`.
    :type arr: list[int]
    :return: The index of the first occurrence of `1` in the array. If no `1` is found, returns `-1`.
    :rtype: int
    """

    # THE AI was able to understand the code I provided to it without any comments and generate the following documentation
    # which I didn't right nor modify at all! THIS IS CONCERNING!!
    # https://www.geeksforgeeks.org/problems/find-transition-point-1587115620/1
    left, right = 0, len(arr) - 1

    result = -1

    while left <= right:
        middle = (left + right) // 2
        if arr[middle] == 0:
            left = middle + 1
        else:
            # in this case, we store the index of this particular 1 as it may be the transition point
            # this comment was added by me after generating documentation for the function with Jetbrains AI feature
            # to test it and see how good it performs
            result = middle
            right = middle - 1

    return result


if __name__ == "__main__":
    array = [int(x) for x in input().split()]
    print(transition_point(array))
