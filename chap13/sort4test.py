

def find_min(L: list, b: int) -> int:
    """전제 조건: L[b:]는 비어있지 않다.
    L[b:] 내 가장 작은 값의 인덱스를 반환한다. 

    >>> find_min([3, -1, 7, 5], 0)
    1
    >>> find_min([3, -1, 7, 5], 1)
    1
    >>> find_min([3, -1, 7, 5], 2)
    3
    """

    smallest = b  # 지금까지 찾은 가장 작은 항목의 인덱스
    i = b + 1
    while i != len(L):
        if L[i] < L[smallest]:
            # L[i]에서 더 작은 항목을 찾았다.
            smallest = i

        i = i + 1

    return smallest


def selection_sort(L: list) -> None:
    """L 내 항목을 가장 작은 값부터 큰 값 순으로 다시 정렬한다. 

    >>> L = [3, 4, 7, -1, 2, 5]
    >>> selection_sort(L)
    >>> L
    [-1, 2, 3, 4, 5, 7]
    >>> L = []
    >>> selection_sort(L)
    >>> L
    []
    >>> L = [1]
    >>> selection_sort(L)
    >>> L
    [1]
    >>> L = [2, 1]
    >>> selection_sort(L)
    >>> L
    [1, 2]
    >>> L = [1, 2]
    >>> selection_sort(L)
    >>> L
    [1, 2]
    >>> L = [3, 3, 3]
    >>> selection_sort(L)
    >>> L
    [3, 3, 3]
    >>> L = [-5, 3, 0, 3, -6, 2, 1, 1]
    >>> selection_sort(L)
    >>> L
    [-6, -5, 0, 1, 1, 2, 3, 3]
    """

    i = 0

    while i != len(L):
        smallest = find_min(L, i)
        L[i], L[smallest] = L[smallest], L[i]
        i = i + 1

if __name__ == '__main__':
    import doctest
    doctest.testmod()


# from sort4 import selection_sort
# import unittest


# class TestSelectionSort(unittest.TestCase):

#     def test_empty(self):
#         '''Test sorting empty list.'''

#         L = []
#         expected = []
#         selection_sort(L)
#         self.assertEqual(expected, L,
#             "Expected {0} but saw {1}".format(expected, L))

#     def test_one(self):
#         '''Test sorting a list of one value.'''

#         L = [1]
#         expected = [1]
#         selection_sort(L)
#         self.assertEqual(expected, L,
#             "Expected {0} but saw {1}".format(expected, L))

#     def test_two_ordered(self):
#         '''Test sorting an already-sorted list of two values.'''

#         L = [1, 2]
#         expected = [1, 2]
#         selection_sort(L)
#         self.assertEqual(expected, L,
#             "Expected {0} but saw {1}".format(expected, L))

#     def test_two_reversed(self):
#         '''Test sorting a reverse-ordered list of two values.'''

#         L = [2, 1]
#         expected = [1, 2]
#         selection_sort(L)
#         self.assertEqual(expected, L,
#             "Expected {0} but saw {1}".format(expected, L))

#     def test_three_identical(self):
#         '''Test sorting a list of three equal values.'''

#         L = [3, 3, 3]
#         expected = [3, 3, 3]
#         selection_sort(L)
#         self.assertEqual(expected, L,
#             "Expected {0} but saw {1}".format(expected, L))

#     def test_three_split(self):
#         '''Test sorting a list with one number different.'''

#         L = [3, 0, 3]
#         expected = [0, 3, 3]
#         selection_sort(L)
#         self.assertEqual(expected, L,
#             "Expected {0} but saw {1}".format(expected, L))

#     def test_several(self):
#         '''Test sorting a list with several values, some duplicated.'''

#         L = [-5, 3, 0, 3, -6, 2, 1, 1]
#         expected = [-6, -5, 0, 1, 1, 2, 3, 3]
#         selection_sort(L)
#         self.assertEqual(expected, L,
#             "Expected {0} but saw {1}".format(expected, L))

# if __name__ == '__main__':
#     unittest.main()
