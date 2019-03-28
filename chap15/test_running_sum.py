import unittest
import sums as sums

class TestRunningSum(unittest.TestCase):
    """sums.running_sum 테스트."""

    def test_running_sum_empty(self):
        """빈 리스트를 테스트한다."""

        argument = []
        expected = []
        sums.running_sum(argument)
        self.assertEqual(expected, argument, "The list is empty.")

    def test_running_sum_one_item(self):
        """항목이 하나인 리스트를 테스트한다.""" 

        argument = [5]
        expected = [5]
        sums.running_sum(argument)
        self.assertEqual(expected, argument, "The list contains one item.")

    def test_running_sum_two_items(self):
        """항목이 둘인 리스트를 테스트한다.""" 

        argument = [2, 5]
        expected = [2, 7]
        sums.running_sum(argument)
        self.assertEqual(expected, argument, "The list contains two items.")

    def test_running_sum_multi_negative(self):
        """음수만 포함하는 리스트를 테스트한다.""" 

        argument = [-1, -5, -3, -4]
        expected = [-1, -6, -9, -13]
        sums.running_sum(argument)
        self.assertEqual(expected, argument,
            "The list contains only negative values.")

    def test_running_sum_multi_zeros(self):
        """0만 포함하는 리스트를 테스트한다."""

        argument = [0, 0, 0, 0]
        expected = [0, 0, 0, 0]
        sums.running_sum(argument)
        self.assertEqual(expected, argument, "The list contains only zeros.")

    def test_running_sum_multi_positive(self):
        """양수만 포함하는 리스트를 테스트한다.""" 

        argument = [4, 2, 3, 6]
        expected = [4, 6, 9, 15]
        sums.running_sum(argument)
        self.assertEqual(expected, argument,
            "The list contains only positive values.")

    def test_running_sum_multi_mix(self):
        """음수와 0, 양수 값이 섞인 리스트를 테스트한다.""" 

        argument = [4, 0, 2, -5, 0]
        expected = [4, 4, 6, 1, 1]
        sums.running_sum(argument)
        self.assertEqual(expected, argument,
            "The list contains a mixture of negative values, zeros and"
                         + "positive values.")

unittest.main()
