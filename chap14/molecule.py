from atom import Atom

class Molecule:
    """이름과 원자 리스트를 갖는 분자""" 

    def __init__(self, name: str) -> None:
        """어떤 원자도 없는 name이라는 분자를 생성한다. 
        """

        self.name = name
        self.atoms = []

    def add(self, a: Atom) -> None:
        """a를 이 분자의 Atom 리스트에 추가한다. 
        """

        self.atoms.append(a)

    def translate(self, x: float, y: float, z: float) -> None:
        """이 분자의 모든 원자를 (x, y, z)만큼 옮긴다.
        """

        for atom in self.atoms:
            atom.translate(x, y, z)

    def __str__(self) -> str:
        """(NAME, (ATOM1, ATOM2, ...)) 형식으로 이 분자의 문자열 표현을 반환한다.
        """

        res = ''
        for atom in self.atoms:
            res = res + str(atom) + ', '

        # 마지막 쉼표를 제거한다.
        res = res[:-2]
        return '({0}, ({1}))'.format(self.name, res)

    def __repr__(self) -> str:
        """Return a string representation of this Molecule in this format:
          Molecule("NAME", (ATOM1, ATOM2, ...))
        """

        res = ''
        for atom in self.atoms:
            res = res + repr(atom) + ', '

        # Strip off the last comma.
        res = res[:-2]
        return 'Molecule("{0}", ({1}))'.format(self.name, res)


if __name__ == '__main__':
    ammonia = Molecule("AMMONIA")
    ammonia.add(Atom(1, "N", 0.257, -0.363, 0.0))
    ammonia.add(Atom(2, "H", 0.257, 0.727, 0.0))
    ammonia.add(Atom(3, "H", 0.771, -0.727, 0.890))
    ammonia.add(Atom(4, "H", 0.771, -0.727, -0.890))
    ammonia.translate(0, 0, 0.2)
    assert ammonia.atoms[0].center[0] == 0.257
    assert ammonia.atoms[0].center[1] == -0.363
    assert ammonia.atoms[0].center[2] == 0.2
    print(repr(ammonia))
    print(ammonia)
