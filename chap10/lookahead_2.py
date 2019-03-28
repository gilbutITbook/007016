from typing import TextIO

def read_molecule(reader: TextIO, line: str) -> list:
    """reader에서 분자 하나를 읽는데, 이때 line은 읽으려는 분자의 첫 번째 줄을
    참조한다. 분자와 그 분자 다음에 나오는 첫 번째 줄(파일 끝이면 빈 문자열)을 
    반환한다. 
    """ 

    fields = line.split()
    molecule = [fields[1]]


    line = reader.readline()
    while line and not line.startswith('COMPND'):
        fields = line.split()
        if fields[0] == 'ATOM':
            key, num, atom_type, x, y, z = fields
            molecule.append([atom_type, x, y, z])
        line = reader.readline()

    return molecule, line
