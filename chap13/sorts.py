def find_min(L: list, b: int) -> int:
    """전제 조건: L[b:]는 비어있지 않다.
    L[b:] 내 가장 작은 값의 인덱스를 반환한다. 

    >>> find_min([3, -1, 7, 5], 0)
    1
    >>> find_min([3, -1, 7, 5], 1)
    1
    >>> find_min([3, -1, 7, 5], 2)
    3
    """

    smallest = b  # 지금까지 찾은 가장 작은 항목의 인덱스
    i = b + 1
    while i != len(L):
        if L[i] < L[smallest]:
            # L[i]에서 더 작은 항목을 찾았다.
            smallest = i

        i = i + 1

    return smallest


def selection_sort(L: list) -> None:
    """L 내 항목을 가장 작은 값부터 큰 값 순으로 다시 정렬한다. 

    >>> L = [3, 4, 7, -1, 2, 5]
    >>> selection_sort(L)
    >>> L
    [-1, 2, 3, 4, 5, 7]
    """

    i = 0
    while i != len(L):
        smallest = find_min(L, i)
        L[i], L[smallest] = L[smallest], L[i]
        i = i + 1


def insert(L: list, b: int) -> None:
    """전제 조건: L[0:b]는 정렬돼 있다.
    L[0:b + 1] 내 올바른 위치에 L[b]를 삽입한다. 

    >>> L = [3, 4, -1, 7, 2, 5]
    >>> insert(L, 2)
    >>> L
    [-1, 3, 4, 7, 2, 5]
    >>> insert(L, 4)
    >>> L
    [-1, 2, 3, 4, 7, 5]
    """

    # L[b]에서 거꾸로 더 작은 항목을 찾아서 L[b]를 삽입할 위치를 찾는다. 
    i = b
    while i != 0 and L[i - 1] >= L[b]:
        i = i - 1

    # L[b]를 인덱스 i로 옮기고 이어지는 값들은 오른쪽으로 시프트한다.
    value = L[b]
    del L[b]
    L.insert(i, value)


def insertion_sort(L: list) -> None:
    """L 내 항목을 가장 작은 값부터 큰 값 순으로 다시 정렬한다.

    >>> L = [3, 4, 7, -1, 2, 5]
    >>> insertion_sort(L)
    >>> L
    [-1, 2, 3, 4, 5, 7]
    """

    i = 0
    while i != len(L):
        insert(L, i)
        i = i + 1


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


def mergesort(L: list) -> None:
    """항목을 가장 작은 값부터 큰 값 순으로 다시 정렬한다.

    >>> L = [3, 4, 7, -1, 2, 5]
    >>> mergesort(L)
    >>> L
    [-1, 2, 3, 4, 5, 7]
    """

    # 병합을 시작할 수 있도록 한 항목짜리 리스트들의 리스트를 만든다.
    workspace = []
    for i in range(len(L)):
        workspace.append([L[i]])

    # 병합할 다음 두 리스트는 workspace[i]와 workspace[i + 1]이다.
    i = 0

    # 병합할 리스트가 두 개 이상 남아 있으면 병합한다.
    while i < len(workspace) - 1:
        L1 = workspace[i]
        L2 = workspace[i + 1]
        newL = merge(L1, L2)
        workspace.append(newL)
        i += 2

    # 결과를 다시 L에 복사한다.
    if len(workspace) != 0:
        L[:] = workspace[-1][:]

if __name__ == '__main__':
    import doctest
    doctest.testmod()
