from unittest import TestCase
from transition_point import transition_point


class TestTransitionPoint(TestCase):
    def test_normal_transition_point(self):
        array = [0, 0, 0, 1, 1, 1]
        self.assertEqual(transition_point(array), 3)

        array = [0, 0, 0, 0, 0, 1, 1, 1]
        self.assertEqual(transition_point(array), 5)

        array = [0, 1, 1, 1, 1]
        self.assertEqual(transition_point(array), 1)

        array = [0, 0, 0, 0, 1]
        self.assertEqual(transition_point(array), 4)

        array = [0] * 20 + [1]
        self.assertEqual(transition_point(array), 20)

        array = [0] + [1] * 20
        self.assertEqual(transition_point(array), 1)

        array = [0] * 15 + [1] * 100
        self.assertEqual(transition_point(array), 15)

    def test_all_ones(self):
        array = [1, 1, 1, 1]
        self.assertEqual(transition_point(array), 0)

        array = [1, 1, 1, 1, 1]
        self.assertEqual(transition_point(array), 0)

        array = [1] * 50
        self.assertEqual(transition_point(array), 0)

        array = [1]
        self.assertEqual(transition_point(array), 0)

    def test_all_zeros(self):
        array = [0, 0, 0, 0, 0]
        self.assertEqual(transition_point(array), -1)

        array = [0, 0]
        self.assertEqual(transition_point(array), -1)

        array = [0] * 50
        self.assertEqual(transition_point(array), -1)

        array = [0]
        self.assertEqual(transition_point(array), -1)
