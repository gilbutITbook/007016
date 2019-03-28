from typing import Any

def linear_search(lst: list, value: Any) -> int:
    """… 이전과 동일한 독스트링 …
    """

    # 센티넬을 추가한다.
    lst.append(value)

    i = 0

    # value를 찾을 때까지 반복한다.
    while lst[i] != value:
        i = i + 1

    # 센티넬을 제거한다.
    lst.pop()

    # 리스트 끝까지 갔으면 value를 찾지 못한 것이다.
    if i == len(lst):
        return -1
    else:
        return i
