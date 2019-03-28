
def find_largest(n: int, L: list) -> list:
    """L에서 가장 큰 값 n개를 작은 값부터 큰 값 순으로 반환한다.

    >>> L = [3, 4, 7, -1, 2, 5]
    >>> find_largest(3, L)
    [4, 5, 7]
    """

    copy = sorted(L)
    return copy[-n:]

if __name__ == '__main__':
    import doctest
    doctest.testmod()
