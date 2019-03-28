from typing import List

def average(values: List[float]) -> float:
    """values 내 수들의 평균을 반환한다. values 내 어떤 항목은 None일 수 있는데, 
    None 값은 평균을 계산할 때 제외한다.

    >>> average([20, 30])
    25.0
    >>> average([None, 20, 30])
    25.0
    """

    count = 0 # 지금까지 본 값들의 개수 
    total = 0 # 지금까지 본 값들의 합 
    for value in values:
        if value is not None:
            total += value

        count += 1

    return total / count

if __name__ == '__main__':
    import doctest
    doctest.testmod()
