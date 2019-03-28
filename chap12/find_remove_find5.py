from typing import List, Tuple

def find_two_smallest(L: List[float]) -> Tuple[int, int]:
    """리스트 L에서 가장 작은 두 값의 인덱스를 튜플로 반환한다.

    >>> items = [809, 834, 477, 478, 307, 122, 96, 102, 324, 476]
    >>> find_two_smallest(items)
    (6, 7)
    >>> items == [809, 834, 477, 478, 307, 122, 96, 102, 324, 476]
    True
    """

    # 가장 작은 항목의 인덱스를 구해서 그 항목을 삭제한다.
    smallest = min(L)
    min1 = L.index(smallest)
    L.remove(smallest)

    # 다음으로 가장 작은 항목의 인덱스를 구한다.
    next_smallest = min(L)
    min2 = L.index(next_smallest)

    # 가장 작은 항목을 L에 다시 넣는다.
    L.insert(min1, smallest)

    # 삭제와 재삽입으로 인덱스가 바뀌었다면 min2를 수정한다.
    if min1 <= min2:
        min2 += 1

    return (min1, min2)
