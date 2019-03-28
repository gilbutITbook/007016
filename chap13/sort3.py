def selection_sort(L: list) -> None:
    """L 내 항목을 가장 작은 값부터 큰 값 순으로 다시 정렬한다. 

    >>> L = [3, 4, 7, -1, 2, 5]
    >>> selection_sort(L)
    >>> L
    [-1, 2, 3, 4, 5, 7]
    """

    i = 0
    while i != len(L):
        # L[i:]에서 가장 작은 항목의 인덱스를 찾는다.
        L[i], L[smallest] = L[smallest], L[i]
        i = i + 1
