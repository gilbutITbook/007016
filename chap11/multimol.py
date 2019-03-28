from typing import TextIO, Tuple, List, Dict
from io import StringIO

Atom = Tuple[str, Tuple[str, str, str]]
CompoundDict = Dict[str, Atom]


def read_molecule(reader: TextIO) -> CompoundDict:
    """reader에서 분자 하나를 읽어 반환하거나 None을 반환해 파일이 끝났음을 
    알린다. 결과 내 첫 번째 항목은 분자명이고, 각 리스트는 원자 타입과 원자의 
    X, Y, Z 좌표다. 

    >>> instring = 'COMPND TEST\\nATOM 1 N 0.1 0.2 0.3\\nATOM 2 N 0.2 0.1 0.0\\nEND\\n'
    >>> infile = StringIO(instring)
    >>> read_molecule(infile)
    {'TEST': [('N', ('0.1', '0.2', '0.3')), ('N', ('0.2', '0.1', '0.0'))]}
    """

    # If there isn't another line, we're at the end of the file.
    line = reader.readline()
    if not line:
        return None

    # Name of the molecule: "COMPND   name"
    key, name = line.split()

    # Other lines are either "END" or "ATOM num atom_type x y z"
    molecule = {name: []}

    reading = True
    while reading:
        line = reader.readline()
        if line.startswith('END'):
            reading = False
        else:
            key, num, atom_type, x, y, z = line.split()
            molecule[name].append((atom_type, (x, y, z)))

    return molecule


def read_all_molecules(reader: TextIO) -> CompoundDict:
    """reader에서 0개 이상의 분자를 읽어 분자 정보 리스트를 반환한다. 

    >>> cmpnd1 = 'COMPND T1\\nATOM 1 N 0.1 0.2 0.3\\nATOM 2 N 0.2 0.1 0.0\\nEND\\n'
    >>> cmpnd2 = 'COMPND T2\\nATOM 1 A 0.1 0.2 0.3\\nATOM 2 A 0.2 0.1 0.0\\nEND\\n'
    >>> infile = StringIO(cmpnd1 + cmpnd2)
    >>> result = read_all_molecules(infile)
    >>> result['T1']
    [('N', ('0.1', '0.2', '0.3')), ('N', ('0.2', '0.1', '0.0'))]
    >>> result['T2']
    [('A', ('0.1', '0.2', '0.3')), ('A', ('0.2', '0.1', '0.0'))]
    """

    # 분자 정보의 딕셔너리.
    result = {}

    reading = True
    while reading:
        next_molecule = read_molecule(reader)
        if next_molecule:  # None is treated as False in an if statement
            result.update(next_molecule)
        else:
            reading = False
    return result


if __name__ == '__main__':
    # import doctest
    # doctest.testmod()
    molecule_file = open('multimol.pdb', 'r')
    molecules = read_all_molecules(molecule_file)
    molecule_file.close()
    print(molecules)
