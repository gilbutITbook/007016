from typing import List

def running_sum(L: List[float]) -> None:
    """원래 항목을 계속해서 더한 합으로 L을 수정한다.

    >>> L = [4, 0, 2, -5, 0]
    >>> running_sum(L)
    >>> L
    [4, 4, 6, 1, 1]
    """

    for i in range(len(L)):
        L[i] = L[i - 1] + L[i]
