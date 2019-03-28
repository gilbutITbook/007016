

def merge(L1: list, L2: list) -> list:
    """정렬된 리스트인 L1과 L2를 새로운 리스트로 병합해서 반환한다.
    >>> merge([1, 3, 4, 6], [1, 2, 5, 7])
    [1, 1, 2, 3, 4, 5, 6, 7]
    """

    newL = []
    i1 = 0
    i2 = 0

    # 각 L1[i1], L2[i2] 항목 쌍에 대해 더 작은 항목을 newL에 복사한다. 
    while i1 != len(L1) and i2 != len(L2):
        if L1[i1] <= L2[i2]:
            newL.append(L1[i1])
            i1 += 1
        else:
            newL.append(L2[i2])
            i2 += 1

    # 두 리스트에서 남은 항목이 있으면 가져온다.
    # 루프 조건으로 인해 두 리스트 중 하나는 비게 된다.
    newL.extend(L1[i1:])
    newL.extend(L2[i2:])
    return newL

if __name__ == '__main__':
    import doctest
    doctest.testmod()
