def method1(arr: list[int], n: int):
    # this was my original solve for the problem, in O(nlogn) complexity
    # https://www.geeksforgeeks.org/problems/rearrange-an-array-with-o1-extra-space3142/1

    add_to = n
    for i in range(n):
        arr[arr[i] % n] += add_to
        add_to += n

    arr.sort()

    for i in range(n):
        arr[i] %= n


def method2(arr: list[int], n: int):
    # Though this method is far more better in only O(n) complexity
    # The modulo operator when giving conditions is really powerful and
    # can simplify really hard rearrangement problems in place!
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
