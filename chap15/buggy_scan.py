from typing import List

def double_preceding(values: List[float]) -> None:
    """리스트 내 각 항목을 바로 앞 항목을 두 배한 값으로 대체하고, 
    첫 번째 항목은 0으로 대체한다.

    >>> L = [1, 2, 3]
    >>> double_preceding(L)
    >>> L
    [0, 2, 4]
    """


    if values != []:
        temp = values[0]
        values[0] = 0
        for i in range(1, len(values)):
            values[i] = 2 * temp
            temp = values[i]
