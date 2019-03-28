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

    def population_density(self):
        """ (Country) -> number

        이 국가의 제곱킬로미터당 인구로 인구 밀도를 반환한다
        """

        return self.population / self.area

    def __str__(self):
        """ (Country) -> str

        이 국가의 문자열 표현을 반환한다.
        """

        return '{0}은/는 인구가 {1} 명이고 면적은 {2} 제곱킬로미터입니다.'.format(
            self.name, self.population, self.area)

if __name__ == '__main__':

    canada = Country('Canada', 34482779, 9984670)
    print(canada.name)
    print(canada.population)
    print(canada.area)

    canada = Country('Canada', 34482779, 9984670)
    usa = Country('United States of America', 313914040, 9826675)
    canada.is_larger(usa)
    print(usa)


