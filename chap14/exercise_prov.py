class Country:
    """이름, 인구, 면적으로 된 국가"""

    def __init__(self, name, pop, area):
        """ (Country, str, int, int) -> NoneType

        Country를 이름 name, 인구 pop와 면적(제곱 킬로미터)로 초기화한다.
        """

        self.name = name
        self.population = pop
        self.area = area

    def is_larger(self, other):
        """ (Country, Country) -> NoneType

        이 국가의 면적이 다른 국가 other의 면적보다
        클 때만 True를 반환한다.
        """

        return self.area > other.area

    def __str__(self):
        """ (Country) -> str

        이 국가의 문자열 표현을 반환한다.
        """

