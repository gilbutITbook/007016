def find_two_smallest(L):
    """ (앞 코드 참고) """

    # 리스트 맨 앞에 가장 작은 두 수가 오도록 리스트를 정렬한 복사본을 구한다.
    temp_list = sorted(L)
    smallest = temp_list[0]
    next_smallest = temp_list[1]

    # 원래 리스트 L에서 두 수의 인덱스를 구한다.
    # 두 인덱스를 반환한다.