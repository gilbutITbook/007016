with open('hopedale.txt', 'r') as hopedale_file:

    # 설명 줄은 읽고 건너뛴다. 
    hopedale_file.readline()

    # 계속 읽으면서 실제 데이터가 처음으로 나올 때까지 
    # 주석 줄을 건너뛴다.
    data = hopedale_file.readline().strip()
    while data.startswith('#'):
        data = hopedale_file.readline().strip()

    # 이제 첫 번째 데이터를 얻었다.
    # 총 모피 수를 합산한다.
    total_pelts = int(data)
    
    # 나머지 데이터를 읽는다.
    for data in hopedale_file:
        total_pelts = total_pelts + int(data.strip())

print("Total number of pelts:", total_pelts)
