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

    # 인덱스 0부터 시작해 lst 내 각 인덱스 i에 있는 항목을 검사한다:
    #    lst[i]가 찾고 있는 값인가? 그렇다면 검색을 중지한다.