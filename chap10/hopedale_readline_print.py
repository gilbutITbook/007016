with open('hopedale.txt', 'r') as hopedale_file:

    # 설명 줄은 읽고 건너뛴다. 
    hopedale_file.readline()

    # 계속 읽으면서 실제 데이터가 처음으로 나올 때까지 
    # 주석 줄을 건너뛴다.
    data = hopedale_file.readline().rstrip()
    while data.startswith('#'):
        data = hopedale_file.readline().rstrip()

    # 이제 첫 번째 데이터를 얻었다.
    print(data)

    # 나머지 데이터를 읽는다.
    for data in hopedale_file:
        print(data.rstrip())
