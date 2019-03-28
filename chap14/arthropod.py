class Arthropod(Organism):
    """고정된 다리 개수를 갖는 절지동물"""

    def __init__(self, name, x, y, legs):
        """ (Arthropod, str, int, int, int) -> NoneType

        조수 웅덩이의 위치 (x, y)에 다리 개수 legs를 갖는 절지동물
        """

        Organism.__init__(self, name, x, y)
        self.legs = legs

    def __str__(self):
        """ (Arthropod) -> str

        이 절지동물의 문자열 표현을 반환한다.
        """

        return '({0}, {1}, [{2}, {3}])'.format(self.name, self.legs, self.x, self.y)

    def is_decapod(self):
        """ (Arthropod) -> str

        이 절지동물이 십각류(decapod)이면 True를 반환한다.
        """

        return self.legs == 10

    def leg_count(self):
        """ (Arthropod) -> str

        절지동물의 다리 개수를 반환한다.
        """

        return self.legs
