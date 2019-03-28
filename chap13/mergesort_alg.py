def merge(L1, L2):
    """ (list, list) -> list

    정렬된 리스트인 L1과 L2를 새로운 리스트로 병합해서 반환한다.
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


def mergesort(L):
    """ (list) -> NoneType

    리스트 L을 오름차순으로 정렬한다.
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

    L = []
    print "befor", L
    mergesort(L)
    print "after", L

    L = [1]
    print "befor", L
    mergesort(L)
    print "after", L

    L = [5, 4, 2, 3, 6, 1]
    print "befor", L
    mergesort(L)
    print "after", L
