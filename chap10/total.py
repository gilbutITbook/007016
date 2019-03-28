from typing import TextIO
from io import StringIO

def sum_number_pairs(input_file: TextIO, output_file: TextIO) -> None:
    """한 줄에 공백으로 구분된 두 실수가 들어 있는 input_file에서
    데이터를 읽는다. 쓰기를 할 output_file에는 input_file 내 각 줄에 대해 
    input_file에 나오는 두 실수와 공백, 그리고 두 실수의 합을 한 줄로 작성한다.
    """ 

    for number_pair in input_file:
        number_pair = number_pair.strip()
        operands = number_pair.split()
        total = float(operands[0]) + float(operands[1])
        new_line = '{0} {1}\n'.format(number_pair, total)
        output_file.write(new_line)

if __name__ == '__main__':
    with open('number_pairs.txt', 'r') as input_file, \
            open('number_pair_sums.txt', 'w') as output_file:
        sum_number_pairs(input_file, output_file)
