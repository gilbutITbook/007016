import bisect

def bin_sort(values):
    """값을 배열 내부에서 정렬한다. 문제가 발생하는 버전"""
    for i in range(1, len(values)):
        bisect.insort_left(values, values[i], 0, i)
