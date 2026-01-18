from unittest import TestCase

from stock_span_problem import stock_span_problem, stock_span_problem_better_solution


class TestStockSpanProblem(TestCase):
    def test_single_element_array(self):
        array = [42]
        self.assertEqual(stock_span_problem(array), [1])
        self.assertEqual(stock_span_problem_better_solution(array), [1])

        array = [1]
        self.assertEqual(
            stock_span_problem(array), stock_span_problem_better_solution(array)
        )

    def test_increasing_order(self):
        array = [10, 20, 30, 40, 50]
        self.assertEqual(stock_span_problem(array), [1, 2, 3, 4, 5])
        self.assertEqual(stock_span_problem_better_solution(array), [1, 2, 3, 4, 5])

        array = [60, 80, 130, 150, 200, 400, 500, 501]
        self.assertListEqual(
            stock_span_problem(array), stock_span_problem_better_solution(array)
        )

    def test_decreasing_order(self):
        array = [50, 40, 30, 20, 10]
        self.assertEqual(stock_span_problem(array), [1, 1, 1, 1, 1])
        self.assertEqual(stock_span_problem_better_solution(array), [1, 1, 1, 1, 1])

        array = [100, 96, 90, 89, 88, 71, 62]
        self.assertEqual(stock_span_problem(array), [1, 1, 1, 1, 1, 1, 1])
        self.assertEqual(
            stock_span_problem_better_solution(array), [1, 1, 1, 1, 1, 1, 1]
        )

    def test_random_array(self):
        array = [10, 4, 5, 90, 120, 80]
        self.assertEqual(stock_span_problem(array), [1, 1, 2, 4, 5, 1])
        self.assertEqual(stock_span_problem_better_solution(array), [1, 1, 2, 4, 5, 1])

        array = [100, 80, 60, 70, 60, 75, 85]
        self.assertEqual(stock_span_problem(array), [1, 1, 1, 2, 1, 4, 6])
        self.assertEqual(
            stock_span_problem_better_solution(array), [1, 1, 1, 2, 1, 4, 6]
        )

        array = [10, 4, 4, 90, 120, 80]
        self.assertEqual(stock_span_problem(array), [1, 1, 2, 4, 5, 1])
        self.assertEqual(stock_span_problem_better_solution(array), [1, 1, 2, 4, 5, 1])

    def test_all_elements_same(self):
        array = [7, 7, 7, 7]
        self.assertEqual(stock_span_problem(array), [1, 2, 3, 4])
        self.assertEqual(stock_span_problem_better_solution(array), [1, 2, 3, 4])
