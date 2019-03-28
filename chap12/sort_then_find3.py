from typing import List, Tuple

def find_two_smallest(L: List[float]) -> Tuple[int, int]:
    """리스트 L에서 가장 작은 두 값의 인덱스를 튜플로 반환한다.

    >>> items = [809, 834, 477, 478, 307, 122, 96, 102, 324, 476]
    >>> find_two_smallest(items)
    (6, 7)
    >>> items == [809, 834, 477, 478, 307, 122, 96, 102, 324, 476]
    True
    """

    # 리스트 맨 앞에 가장 작은 두 수가 오도록 리스트를 정렬한 복사본을 구한다.
    temp_list = sorted(L)
    smallest = temp_list[0]
    next_smallest = temp_list[1]

    # 원래 리스트 L에서 두 수의 인덱스를 구한다.
    min1 = L.index(smallest)
    min2 = L.index(next_smallest)

    return (min1, min2)
