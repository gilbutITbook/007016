from typing import List, Tuple

def find_two_smallest(L: List[float]) -> Tuple[int, int]:
    """리스트 L에서 가장 작은 두 값의 인덱스를 튜플로 반환한다.

    >>> items = [809, 834, 477, 478, 307, 122, 96, 102, 324, 476]
    >>> find_two_smallest(items)
    (6, 7)
    >>> items == [809, 834, 477, 478, 307, 122, 96, 102, 324, 476]
    True
    """

    # 리스트 내 각 값을 순서대로 확인한다.
    # 지금까지 찾은 가장 작은 두 값의 인덱스를 저장한다.
    # 더 작은 값을 찾으면 인덱스를 업데이트한다.
    # 두 인덱스를 반환한다.
