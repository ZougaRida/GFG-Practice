def method1(arr: list[int], n: int):
    """
    Rearrange the array in place in `O(1)` memory.

    The problem consists of an array of size n, containing all and only values from 0 to
    n - 1, now we need to transform the array in place so that arr[i] = arr[arr[i]].
    This was my initial shot at making that happen and it works. Time complexity
    `O(nlog(n)`

    https://www.geeksforgeeks.org/problems/rearrange-an-array-with-o1-extra-space3142/1

    :param list(int) arr: the list of indices to transform in place
    :param int n: the length of the list
    """

    add_to = n
    for i in range(n):
        arr[arr[i] % n] += add_to
        add_to += n

    arr.sort()

    for i in range(n):
        arr[i] %= n


def method2(arr: list[int], n: int):
    """
    2nd method that uses the wonderful technique of modulo encoding.

    https://www.geeksforgeeks.org/problems/rearrange-an-array-with-o1-extra-space3142/1

    .. note:: now that I think about it, if we keep applying this to the original
              array, eventually we will reach the identity array, in other words,
              arr[i] = i for all i.

    :param list(int) arr: the list of indices to transform in place
    :param int n: the length of the list
    """
    for i in range(n):
        arr[i] += n * (arr[arr[i] % n] % n)

    for i in range(n):
        arr[i] //= n


if __name__ == "__main__":
    array = [int(x) for x in input().split()]
    second_array = array.copy()
    method1(array, len(array))
    print(array)
    method2(second_array, len(second_array))
    print(second_array)
