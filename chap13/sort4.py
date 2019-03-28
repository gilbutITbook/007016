

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
    """

    i = 0
    while i != len(L):
        smallest = find_min(L, i)
        L[i], L[smallest] = L[smallest], L[i]
        i = i + 1

if __name__ == '__main__':
    import doctest
    doctest.testmod()
