import bisect

def bin_sort(values: list) -> list:
    """값을 정렬한 리스트를 반환한다.  (값은 변경하지 않는다.)
    >>> L = [3, 4, 7, -1, 2, 5]
    >>> bin_sort(L)
    [-1, 2, 3, 4, 5, 7]
    """
	
    result = []
    for v in values:
        bisect.insort_left(result, v)

    return result
