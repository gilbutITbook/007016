def find_two_smallest(L):
    """ (앞 코드 참고) """

    # 가장 작은 항목의 인덱스를 구해서 그 항목을 삭제한다.
    smallest = min(L)
    min1 = L.index(smallest)
    L.remove(smallest)

    # 다음으로 가장 작은 항목의 인덱스를 구한다.
    next_smallest = min(L)
    min2 = L.index(next_smallest)

    # 가장 작은 항목을 L에 다시 넣는다.
    # 삭제와 재삽입으로 인덱스가 바뀌었다면 min2를 수정한다.
    # 즉, min1이 min2보다 앞에 있었으면 min2에 1을 더한다.
    # 두 인덱스를 반환한다.
