class Arthropod(Organism):
    """고정된 다리 개수를 갖는 절지동물"""

    def __init__(self, name, x, y, legs):
        """조수 웅덩이의 위치 (x, y)에 다리 개수 legs를 갖는 절지동물"""

        Organism.__init__(self, name, x, y)
        self.legs = legs

    def __str__(self):
        """ (Arthropod) -> str

        이 절지동물의 문자열 표현을 반환한다.
        """

        return '(%s, %s, [%s, %s])' % (self.name, self.legs, self.x, self.y)
