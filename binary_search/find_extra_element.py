def find_extra_element(array1: list[int], array2: list[int]) -> int:
    # https://www.geeksforgeeks.org/problems/index-of-an-extra-element/0

    left, right = 0, len(array1) - 1
    while left < right:
        mid = (left + right) // 2
        if array1[mid] == array2[mid]:
            left = mid + 1
        else:
            right = mid

    return array1[right]


if __name__ == "__main__":
    array1 = [int(x) for x in input().split()]
    array2 = [int(x) for x in input().split()]
    print(find_extra_element(array1, array2))
