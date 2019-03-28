from typing import TextIO
from io import StringIO
import time_series

def smallest_value_skip(reader: TextIO) -> int:
    """time_series 헤더로 시작하는 reader를 읽어서 처리한다.
    헤더 이후에 나오는 가장 작은 값을 반환한다. 
    하이픈으로 표시되는 누락 값은 건너뛴다.

    >>> infile = StringIO('Example\\n1\\n-\\n3\\n')
    >>> smallest_value_skip(infile)
    1
    """

    line = time_series.skip_header(reader).strip()
    # 이제 line에 첫 번째 데이터 값이 들어 있고, 
    # 유일하게 찾은 값이므로 이 값이 현재 가장 작은 값이다.
    smallest = int(line)

    for line in reader:
        line = line.strip()
        if line != '-':
            value = int(line)
            smallest = min(smallest, value)

    return smallest

if __name__ == '__main__':
    with open('hebron.txt', 'r') as input_file:
        print(smallest_value_skip(input_file))
