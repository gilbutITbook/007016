def find_two_smallest(L):
    """ (앞 코드 참고) """

    # 가장 작은 항목의 인덱스를 구해서 그 항목을 삭제한다.
    smallest = min(L)
    min1 = L.index(smallest)
    L.remove(smallest)

    # 다음으로 가장 작은 항목의 인덱스를 구한다.
    next_smallest = min(L)
    min2 = L.index(next_smallest)

    # 가장 작은 항목을 리스트에 다시 넣는다.
    # 필요에 따라 두 번째 인덱스를 조정한다.
    # 두 인덱스를 반환한다.
