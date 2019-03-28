from typing import Any

def linear_search(lst: list, value: Any) -> int:
    """… 이전과 동일한 독스트링 …
    """

    for i in range(len(lst)):
        if lst[i] == value:
            return i

    return -1
