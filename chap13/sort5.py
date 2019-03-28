def insertion_sort(L: list) -> None:
    """L 내 항목을 가장 작은 값부터 큰 값 순으로 다시 정렬한다.

    >>> L = [3, 4, 7, -1, 2, 5]
    >>> insertion_sort(L)
    >>> L
    [-1, 2, 3, 4, 5, 7]
    """

    i = 0
    while i != len(L):
        # L[0:i+1] 내 올바른 위치에 L[i]를 삽입한다.
        i = i + 1
