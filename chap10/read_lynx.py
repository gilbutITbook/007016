from typing import TextIO
from io import StringIO
import time_series

def find_largest(line: str) -> int:
    """'.'으로 끝나는 정수들이 여백으로 구분되어 있는 줄에서 가장 큰 값을  
    반환한다.

    >>> find_largest('1. 3. 2. 5. 2.')
    5
    """
    # 지금까지 찾은 가장 큰 값
    largest = -1
    for value in line.split():
        # 뒤에 붙은 마침표를 제거한다.
        v = int(value[:-1])
        # 더 큰 값을 찾으면 저장한다.
        if v > largest:
            largest = v

    return largest

def process_file(reader: TextIO) -> int:
    """time_series 헤더로 시작하는 reader를 읽고 처리한다. 헤더 이후에 나오는 
    가장 큰 값을 반환한다. 각 줄마다 데이터가 여러 개일 수 있다. 

    >>> infile = StringIO('Example\\n 20. 3.\\n 100. 17. 15.\\n')
    >>> process_file(infile)
    100
    """

    line = time_series.skip_header(reader).strip()
    # 지금까지 가장 큰 값은 첫 번째 줄에 있는 데이터 중 가장 큰 값이다.
    largest = find_largest(line)

    # 나머지 줄을 확인해서 더 큰 값이 있는지 찾는다.
    for line in reader:
        large = find_largest(line)
        if large > largest:
            largest = large
    return largest

if __name__ == '__main__':
    with open('lynx.txt', 'r') as input_file:
        print(process_file(input_file))
