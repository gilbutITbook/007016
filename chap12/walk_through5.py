def find_two_smallest(L):
    """ (앞 코드 참고) """

    # L의 맨 앞부분에서 가장 작은 값과 두 번째로 작은 값의 인덱스를 
    # min1과 min2에 할당한다.
    if L[0] < L[1]:
        min1, min2 = 0, 1
    else:
        min1, min2 = 1, 0

    # 리스트 내 각 값을 순서대로 확인한다.
    for i in range(2, len(L)):
    #     min1과 min2보다 작은 값을 찾거나 
    #     min1 또는 min2보다 작은 값을 찾으면 업데이트한다.
    # 두 인덱스를 반환한다.
