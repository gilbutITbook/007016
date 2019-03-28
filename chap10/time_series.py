from typing import TextIO
from io import StringIO

def skip_header(reader: TextIO) -> str:
    """reader 내 헤더를 건너뛰고 첫 번째 진짜 데이터를 반환한다.

    >>> infile = StringIO('Example\\n# Comment\\n# Comment\\nData line\\n')
    >>> skip_header(infile)
    'Data line\\n'
    """

    # 설명 줄을 읽는다.
    line = reader.readline()

    # 처음으로 주석이 아닌 줄을 찾는다.
    line = reader.readline()
    while line.startswith('#'):
        line = reader.readline()

    # 이제 line에는 첫 번째 진짜 데이터가 들어 있다.
    return line

def process_file(reader: TextIO) -> None:
    """한 줄의 설명, '#'으로 시작하는 여러 줄, 데이터 여러 줄로 구성된 데이터를 
   reader에서 읽어 출력한다. 

    >>> infile = StringIO('Example\\n# Comment\\nLine 1\\nLine 2\\n')
    >>> process_file(infile)
    Line 1
    Line 2
    """

    # 첫 번째 데이터를 찾아 출력한다.
    line = skip_header(reader).strip()
    print(line)

    # 나머지 데이터를 읽는다.
    for line in reader:
        line = line.strip()
        print(line)

if __name__ == '__main__':
    with open('hopedale.txt', 'r') as input_file:
        process_file(input_file)
