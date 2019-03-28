from typing import TextIO 
from io import StringIO 

def read_molecule(reader: TextIO) -> list:
    """reader에서 분자 하나를 읽어 반환하거나 None을 반환해 파일이 끝났음을 
       알린다. 결과 내 첫 번째 항목은 분자명이고, 각 리스트는 원자 타입과 원자의 
       X, Y, Z 좌표다. 
       >>> instring = 'COMPND TEST\\nATOM 1 N 0.1 0.2 0.3\\nATOM 2 N 0.2 0.1 0.0\\nEND\\n'
       >>> infile = StringIO(instring)
       >>> read_molecule(infile)
       ['TEST', ['N', '0.1', '0.2', '0.3'], ['N', '0.2', '0.1', '0.0']]
    """ 

    # 더 이상 줄이 없으면 파일이 끝난 것이다.
    line = reader.readline()
    if not line:
        return None

    # 분자명: "COMPND  name" 
    parts = line.split()
    name = parts[1]

    # 다른 줄은 "END"나 "ATOM num atom_type x y z" 중 하나다.
    molecule = [name]

    reading = True
    while reading:
        line = reader.readline()
        if line.startswith('END'):
            reading = False
        else:
            parts = line.split()
            molecule.append(parts[2:])

    return molecule

def read_all_molecules(reader: TextIO) -> list:
    """reader에서 0개 이상의 분자를 읽어 분자 정보 리스트를 반환한다. 

    >>> cmpnd1 = 'COMPND T1\\nATOM 1 N 0.1 0.2 0.3\\nATOM 2 N 0.2 0.1 0.0\\nEND\\n'
    >>> cmpnd2 = 'COMPND T2\\nATOM 1 A 0.1 0.2 0.3\\nATOM 2 A 0.2 0.1 0.0\\nEND\\n'
    >>> infile = StringIO(cmpnd1 + cmpnd2)
    >>> result = read_all_molecules(infile)
    >>> result[0]
    ['T1', ['N', '0.1', '0.2', '0.3'], ['N', '0.2', '0.1', '0.0']]
    >>> result[1]
    ['T2', ['A', '0.1', '0.2', '0.3'], ['A', '0.2', '0.1', '0.0']]
    """

    # 분자 정보 리스트
    result = []

    reading = True
    while reading:
        molecule = read_molecule(reader)
        if molecule:  #  None은 if 문에서 False로 간주된다.
            result.append(molecule)
        else:
            reading = False
    return result

if __name__ == '__main__':
    molecule_file = open('multimol.pdb', 'r')
    molecules = read_all_molecules(molecule_file)
    molecule_file.close()
    print(molecules)
