"""이진 검색을 테스트한다."""

import unittest
from binary_search import binary_search

# 검색할 리스트
VALUES = [1, 3, 4, 4, 5, 7, 9, 10]


class TestBS(unittest.TestCase):
    def test_first(self):
        """리스트의 처음에 있는 값을 테스트한다."""

        expected = 0
        actual = binary_search(VALUES, 1)
        self.assertEqual(expected, actual,
            "Error searching for {0}".format(expected))

    def test_duplicate(self):
        """중복 값을 테스트한다."""

        expected = 2
        actual = binary_search(VALUES, 4)
        self.assertEqual(expected, actual,
            "Error searching for {0}".format(expected))

    def test_middle(self):
        """중간 값을 위한 검색을 테스트한다."""

        expected = 4
        actual = binary_search(VALUES, 5)
        self.assertEqual(expected, actual,
            "Error searching for {0}".format(expected))

    def test_last(self):
        """마지막 값을 위한 검색을 테스트한다."""

        expected = 7
        actual = binary_search(VALUES, 10)
        self.assertEqual(expected, actual,
            "Error searching for {0}".format(expected))

    def test_missing_start(self):
        """Test searching for a missing value at the start."""

        expected = -1
        actual = binary_search(VALUES, -3)
        self.assertEqual(expected, actual,
            "Error searching for {0}".format(expected))

    def test_missing_middle(self):
        """Test searching for a missing value in the middle."""

        expected = -1
        actual = binary_search(VALUES, 2)
        self.assertEqual(expected, actual,
            "Error searching for {0}".format(expected))

    def test_missing_end(self):
        """Test searching for a missing value at the end."""

        expected = -1
        actual = binary_search(VALUES, 11)
        self.assertEqual(expected, actual,
            "Error searching for {0}".format(expected))

if __name__ == '__main__':
    unittest.main()
