from typing import Annotated
from annotated_types import Gt

type positive_int = Annotated[int, Gt(0)]


def stock_span_problem(arr: list[positive_int]) -> list[positive_int]:
    """
    This function consists of finding in simpler terms the first max from left of each
    arr[i] or rather getting back its index, of course if it exists.

    I admit this was by far the solution I was able to get at first which is very
    straightforward to implement once understood that we need to get the first max
    from left

    Time Complexity: :math:`O(n^2)` and Memory Complexity: `O(1)`

    https://www.geeksforgeeks.org/problems/stock-span-problem-1587115621/1

    :param list[int] arr: The list of positive integers representing stock prices in
                          each day i
    :return: a list containing the span of each day i
    :rtype: list[int]
    """
    n = len(arr)

    # for span of first day, it's obviously 1
    spans_array = [1]
    for i in range(1, n):
        span_i = 1
        j = i - 1
        while j >= 0 and arr[j] <= arr[i]:
            span_i += 1
            j -= 1

        spans_array.append(span_i)
    return spans_array


def stock_span_problem_better_solution(arr: list[positive_int]) -> list[positive_int]:
    """
    2nd version of the solution to stock span problem with better time complexity.

    This method is honestly really powerful, had maybe some initial guess to how it
    goes, but definitely didn't come with its solution, the idea is to create a
    temporary stack, a special stack that keeps track of the
    latest values to which we counted the span, so that next element that comes,
    either we use the previous elements and pop them out then append the new value,
    or keep them there and append the new span of value 1 along with them too.

    **REMEMBER WELL THIS USEFUL TECHNIQUE!**

    Time Complexity: `O(n)` and Memory Complexity: `O(1)`

    https://www.geeksforgeeks.org/problems/stock-span-problem-1587115621/1

    :param list[int] arr: The list of positive integers representing stock prices in
                          each day i
    :return: the list containing the span of each day i
    :rtype: list[int]

    """
    n = len(arr)

    # again the span of first day is obviously 1
    results = [1]

    # for the stack we keep track of the index since we'll need that to access both
    # the price of the stock at day i and the span at that same day if needed
    stack = [0]

    for i in range(1, n):
        span_i = 1
        while stack and arr[i] >= arr[stack[-1]]:
            span_i += results[stack[-1]]
            stack.pop()

        stack.append(i)
        results.append(span_i)

    return results


if __name__ == "__main__":
    array = [int(x) for x in input().split()]
    print(stock_span_problem(array))
    print(stock_span_problem_better_solution(array))
