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
