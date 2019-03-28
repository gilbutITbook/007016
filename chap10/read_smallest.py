from typing import TextIO
import time_series

def smallest_value(reader: TextIO) -> int:
    """reader를 읽어서 처리하고, time_series 헤더 이후에 나오는 가장 작은 값을 
    반환한다.

    >>> infile = StringIO('Example\\n1\\n2\\n3\\n')
    >>> smallest_value(infile)
    1
    >>> infile = StringIO('Example\\n3\\n1\\n2\\n')
    >>> smallest_value(infile)
    1
    """

    line = time_series.skip_header(reader).strip()

    # 이제 line에 첫 번째 데이터 값이 들어 있고, 
    # 유일하게 찾은 값이므로 이 값이 현재 가장 작은 값이다. 
    smallest = int(line)

    for line in reader:
        value = int(line.strip())

        # 더 작은 값을 찾으면 저장한다.
        if value < smallest:
            smallest = value

    return smallest

if __name__ == '__main__':
    with open('hopedale.txt', 'r') as input_file:
        print(smallest_value(input_file))
