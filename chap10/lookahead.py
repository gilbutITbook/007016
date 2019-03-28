from lookahead_2 import read_molecule
from typing import TextIO

def read_all_molecules(reader: TextIO) -> list:
    """reader에서 0개 이상의 분자를 읽고 읽어들인 분자 리스트를 반환한다.
    """ 

    result = []
    line = reader.readline()
    while line:
        molecule, line = read_molecule(reader, line)
        result.append(molecule)

    return result
