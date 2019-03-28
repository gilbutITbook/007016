from typing import TextIO

def read_molecule(reader: TextIO) -> list:
    """reader에서 분자 하나를 읽어 반환하거나 None을 반환해 파일이 끝났음을 
       알린다. 결과 내 첫 번째 항목은 분자명이고, 각 리스트는 원자 타입과 원자의     X, Y, Z 좌표다. 
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
