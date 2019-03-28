class Organism:
    """조수 웅덩이에 사는 유기체."""

    def __init__(self, name, x, y):
        """ (Organism, str, int, int) -> NoneType

        조수 웅덩이 (x,y) 위치에 사는 유기체."""

        self.name = name
        self.x = x
        self.y = y

    def __str__(self):
        """ (Organism) -> str

        유기체의 문자열 표현을 반환한다.
        """

        return '({0}, [{1}, {2}])'.format(self.name, self.x, self.y)

    def can_eat(self, food):
        """ (Organism, str) -> bool

        유기체가 제공된 음식을 먹을 수 있는지 알려준다.
        일반적인 유기체가 무엇을 먹는지 알 수 없으므로
        이 함수는 항상 False를 반환한다.
        """

        return False

    def move(self):
        """ (Organism) -> NoneType

        유기체가 이동할 수 있는지 확인한다.
        일반적인 유기체가 얼마나 빨리, 얼마나 멀리 이동할 수 있는지
        알 수 없으므로 이 함수는 아무것도 하지 않습니다.
        """

        return
