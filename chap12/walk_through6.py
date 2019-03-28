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
    #
    #    L[i]는 min1과 min2보다 작거나, 둘 사이거나, 둘보다 크다. 
    #    L[i]가 min1과 min2보다 작으면 둘 다 업데이트한다.
    #    L[i]가 min1과 min2 사이면 min2를 업데이트한다.
    #    L[i]가 min1과 min2보다 크면 아무것도 하지 않는다.
	
    return (min1, min2)
