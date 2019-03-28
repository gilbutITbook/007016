from typing import List, Tuple

def find_two_smallest(L: List[float]) -> Tuple[int, int]:
    """리스트 L에서 가장 작은 두 값의 인덱스를 튜플로 반환한다.

    >>> items = [809, 834, 477, 478, 307, 122, 96, 102, 324, 476]
    >>> find_two_smallest(items)
    (6, 7)
    >>> items == [809, 834, 477, 478, 307, 122, 96, 102, 324, 476]
    True
    """

    # L의 복사본을 정렬한다.
    # 가장 작은 두 수를 구한다.
    # 원래 리스트 L에서 두 수의 인덱스를 구한다.
    # 두 인덱스를 반환한다.
