class Arthropod(Organism):
    """고정된 다리 개수를 갖는 절지동물"""

    def __init__(self, name, x, y, legs):
        """ (Arthropod, str, int, int, int) -> NoneType

        조수 웅덩이의 위치 (x, y)에 다리 개수 legs를 갖는 절지동물
        """

        Organism.__init__(self, name, x, y)
        self.legs = legs
