def find_min_max(values: list):
    """values에서 최솟값과 최댓값을 출력한다. 
    """

    min = None
    max = None
    for value in values:
        if value > max:
            max = value
        if value < min:
            min = value

    print('최솟값은 {0}입니다'.format(min))
    print('최댓값은 {0}입니다'.format(max))
