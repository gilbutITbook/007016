from molecule import Molecule
from atom import Atom
from typing import TextIO

def read_molecule(r: TextIO) -> Molecule:
    """r로부터 분자 하나를 읽어 반환하거나 파일 끝에 도달하면 None을 반환한다.
    """
    # 더 이상 줄이 없으면 파일 끝에 도달한 것이다. 
    line = r.readline()
    if not line:
        return None

    # 분자명: "COMPND name" 
    key, name = line.split()

    # 그 밖에 줄은 "END" 또는 "ATOM num kind x y z"이다.
    molecule = Molecule(name)
    reading = True

    while reading:
        line = r.readline()
        if line.startswith('END'):
            reading = False
        else:
            key, num, kind, x, y, z = line.split()
            molecule.add(Atom(int(num), kind, float(x), float(y), float(z)))

    return molecule
