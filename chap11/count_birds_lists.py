from typing import TextIO, List, Any
from io import StringIO

def count_birds(observations_file: TextIO) -> List[List[Any]]:
    """한 줄당 새 종이 하나씩 나열된 관찰 파일에서 새 종 세트를 반환한다. 

    >>> infile = StringIO('bird 1\\nbird 2\\nbird 1\\n')
    >>> count_birds(infile)
    [['bird 1', 2], ['bird 2', 1]]
    """
    bird_counts = []
    for line in observations_file:
        bird = line.strip()
        found = False
        # bird_counts 리스트에서 새를 찾는다. 
        for entry in bird_counts:
            if entry[0] == bird:
                entry[1] = entry[1] + 1
                found = True
        if not found:
            bird_counts.append([bird, 1])

    return bird_counts

if __name__ == '__main__':
    with open('observations.txt') as observations_file:
        bird_counts = count_birds(observations_file)

        # 각 새와 관찰된 횟수를 출력한다.
        for entry in bird_counts:
            print(entry[0], entry[1])
