

def insert(L: list, b: int) -> None:
    """전제 조건: L[0:b]는 정렬돼 있다.
    L[0:b + 1] 내 올바른 위치에 L[b]를 삽입한다. 

    >>> L = [3, 4, -1, 7, 2, 5]
    >>> insert(L, 2)
    >>> L
    [-1, 3, 4, 7, 2, 5]
    >>> insert(L, 4)
    >>> L
    [-1, 2, 3, 4, 7, 5]
    """

    # L[b]에서 거꾸로 더 작은 항목을 찾아서 L[b]를 삽입할 위치를 찾는다. 
    i = b
    while i != 0 and L[i - 1] >= L[b]:
        i = i - 1

    # L[b]를 인덱스 i로 옮기고 이어지는 값들은 오른쪽으로 시프트한다.
    value = L[b]
    del L[b]
    L.insert(i, value)

def insertion_sort(L: list) -> None:
    """L 내 항목을 가장 작은 값부터 큰 값 순으로 다시 정렬한다.

    >>> L = [3, 4, 7, -1, 2, 5]
    >>> insertion_sort(L)
    >>> L
    [-1, 2, 3, 4, 5, 7]
    """

    i = 0

    while i != len(L):
        insert(L, i)
        i = i + 1

if __name__ == '__main__':
    import doctest
    doctest.testmod()
