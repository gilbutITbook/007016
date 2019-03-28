def print_table(n: int) -> None:
    """1부터 n까지 곱셈표를 출력한다.

    >>> print_table(5)
        1       2       3       4       5
    1   1       2       3       4       5
    2   2       4       6       8       10
    3   3       6       9       12      15
    4   4       8       12      16      20
    5   5       10      15      20      25
    """
    # 표에 포함되는 수들
    numbers = list(range(1, n + 1))

    # 헤더 행을 출력한다.
    for i in numbers:
        print('\t' + str(i), end='')

    # 헤더 행을 끝낸다.
    print()

    # 각 행 번호와 그 행의 내용을 출력한다.
    for i in numbers:  #(1)

        print (i, end='')  #(2)
        for j in numbers:   #(3)
            print('\t' + str(i * j), end='') #(4)

        # 현재 행을 끝낸다. 
        print() #(5)
