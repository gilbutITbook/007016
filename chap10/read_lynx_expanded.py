from typing import TextIO
from io import StringIO

def process_file(reader: TextIO) -> int:
    """time_series 헤더로 시작하는 reader를 읽고 처리한다. 헤더 이후에 나오는 
    가장 큰 값을 반환한다. 각 줄마다 데이터가 여러 개일 수 있다.

    >>> infile = StringIO('Example\\n 20. 3.\\n')
    >>> process_file(infile)
    20
    >>> infile = StringIO('Example\\n 20. 3.\\n 100. 17. 15.\\n')
    >>> process_file(infile)
    100
    """

    # 설명 줄을 읽는다.
    line = reader.readline()

    # 주석이 아닌 첫 번째 줄을 찾는다.
    line = reader.readline() 
    while line.startswith('#'): 
        line = reader.readline()
    # 이제 line에 첫 번째 진짜 데이터가 들어 있다. 
    # 현재 줄에서 지금까지 가장 큰 값
    largest = -1
    for value in line.split(): 
    
        # 뒤에 붙은 마침표를 제거한다.
        v = int(value[:-1])

        # 더 큰 값을 찾으면 저장한다.
        if v > largest: 
            largest = v 
    
    # 나머지 줄을 확인해서 더 큰 값이 있는지 찾는다.
    for line in reader:
        
        # 현재 줄에서 지금까지 가장 큰 값
        largest_in_line = -1
        for value in line.split(): 
        
            # 뒤에 붙은 마침표를 제거한다.
            v = int(value[:-1])
            # 더 큰 값을 찾으면 저장한다.
            if v > largest_in_line: 
                largest_in_line = v 
        if largest_in_line > largest: 
            largest = largest_in_line 
    return largest
    
if __name__ == '__main__':
    with open('lynx.txt', 'r') as input_file: 
        print(process_file(input_file))
        