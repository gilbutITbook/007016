from typing import Any

def linear_search(lst: list, value: Any) -> int:
    """lst에서 value가 처음으로 나오는 인덱스를 반환하거나 lst에 value가 없으면 
    -1을 반환한다. 

    >>> linear_search([2, 5, 1, -3], 5)
    1
    >>> linear_search([2, 4, 2], 2)
    0
    >>> linear_search([2, 5, 1, -3], 4)
    -1
    >>> linear_search([], 5)
    -1
    """

    i = 0  # lst 내에서 검사할 다음 항목의 인덱스 

    # lst 끝에 도달하거나 value를 찾을 때까지 반복한다.
    while i != len(lst) and lst[i] != value:
        i = i + 1

    # 리스트 끝까지 갔으면 value를 찾지 못한 것이다.
    if i == len(lst):
        return -1
    else:
        return i
