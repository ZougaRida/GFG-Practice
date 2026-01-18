def stock_span_problem(arr: list[int]) -> list[int]:
    """
    This function consists on finding in simpler terms the first max from left of each arr[i]
    or rather getting back its index, of course if it exists.
    I admit this was by far the solution I was able to get at first which is very straightforward to implement.
    once understood that we need to get the first max from left

    Time Complexity: O(n^2) and Memory Complexity: O(1)

    https://www.geeksforgeeks.org/problems/stock-span-problem-1587115621/1
    """
    n = len(arr)
    first_max_from_left = [1]
    for i in range(1, n):
        for j in range(1, i + 1):
            if arr[i - j] > arr[i]:
                first_max_from_left.append(j)
                break

            if i - j == 0:
                first_max_from_left.append(j + 1)
    return first_max_from_left


def stock_span_problem_better_solution(arr: list[int]) -> list[int]:
    """
    This method is honestly really powerful, had maybe some initial guess to how it goes but definitely
    didn't come with its solution, the idea is to create a temporary stack, a special monotonic decreasing stack
    that keeps track of the latest values to which we counted the span, so that next element that comes, either we
    use that and pop them out and keep track of their values in the new appended indeed, or keep them there and append
    the min value along with them to
    REMEMBER WELL THIS USEFUL TECHNIQUE!



    """
    n = len(arr)
    result = []
    stack = []

    for i in range(n):
        while stack and arr[stack[-1]] <= arr[i]:
            stack.pop()

        if stack:
            result.append(i - stack[-1])
        else:
            result.append(i + 1)

        stack.append(i)
    return result


if __name__ == "__main__":
    array = [int(x) for x in input().split()]
    print(stock_span_problem(array))
    print(stock_span_problem_better_solution(array))
