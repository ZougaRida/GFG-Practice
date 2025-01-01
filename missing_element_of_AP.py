def find_missing(arr: list[int]) -> int:
    """
    Find the missing element of the arithmetic progression.

    The right most element and leftmost element are the boundaries to look for the missing element since array is sorted.
    Recall for the AP we have a_n = a_0 + nk where k is that step of AP.
    Note that the boundary is absolutely given, thus the missing element a_k must be in between.
    https://www.geeksforgeeks.org/problems/missing-element-of-ap2228/1

    :param arr: the sorted list of numbers forming the arithmetic progression
    :type arr: list[int]
    :return: the missing element of the arithmetic progression
    :rtype: int
    """
    n = len(arr)
    # you might think that we should devide only by n - 1 to get the k of AP
    # since a_0 is already the first element
    # though the rightmost term is a_n not a_n-1
    # since there is the missing term in between them to look for
    k = (arr[n - 1] - arr[0]) // n

    left, right = 0, n - 1
    while left < right:
        middle = (left + right) // 2
        if arr[middle] == arr[0] + middle * k:
            left = middle + 1
        else:
            right = middle

    return arr[0] + right * k


if __name__ == "__main__":
    array = [int(x) for x in input().split()]
    print(find_missing(array))
