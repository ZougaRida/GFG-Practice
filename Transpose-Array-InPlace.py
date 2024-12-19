def method1(arr, n):
    add_to = n
    for i in range(n):
        arr[arr[i] % n] += add_to
        add_to += n

    arr.sort()

    for i in range(n):
        arr[i] %= n


def method2(arr, n):
    for i in range(n):
        arr[i] += n * (arr[arr[i] % n] % n)

    for i in range(n):
        arr[i] //= n


array = [int(x) for x in input().split()]
second_array = array.copy()
method1(array, len(array))
print(array)
method2(second_array, len(second_array))
print(second_array)