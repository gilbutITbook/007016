class Atom:
    """ 번호와 기호, 좌표를 갖는 원자 """ 

    def __init__(self, num: int, sym: str, x: float, y: float,
                 z: float) -> None:
        """원자 번호인 num, 문자열 기호인 sym, 실수로 된 (x, y, z) 좌표를 사용해 
        Atom을 생성한다.
        """

        self.number = num
        self.center = (x, y, z)
        self.symbol = sym

    def translate(self, x: float, y: float, z: float) -> None:
    """이 원자의 좌표에 (x, y, z)를 더해서 원자를 이동시킨다. 
    """ 

        self.center = (self.center[0] + x,
                       self.center[1] + y,
                       self.center[2] + z)

    def __str__(self) -> str:
    """(SYMBOL, X, Y, Z) 형식으로 Atom의 문자열 표현을 반환한다.
    """

        return '({0}, {1}, {2}, {3})'.format(
            self.symbol, self.center[0], self.center[1], self.center[2])

    def __repr__(self) -> str:
    """Atom(NUMBER, "SYMBOL", X, Y, Z) 형식으로 Atom의 문자열 표현을 반환한다.
    """

        return 'Atom({0}, "{1}", {2}, {3}, {4})'.format(
            self.number, self.symbol,
            self.center[0], self.center[1], self.center[2])

if __name__ == '__main__':
    nitrogen = Atom(1, "N", 0.257, -0.363, 0.0)
    nitrogen.translate(0, 0, 0.2)
