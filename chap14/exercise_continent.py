import exercise_country as country

class Continent:

    def __init__(self, name, countries):
        """ (Continent, str, list of Country) -> NoneType

       대륙명 name과 국가 리스트 countries로 초기화한다.
        """

        self.name = name
        self.countries = countries


    def total_population(self):
        """ (Continent) -> int

        대륙의 인구수를 반환한다.
        """

        pop = 0
        for country in self.countries:
            pop += country.population

        return pop

    def __str__(self):
        """ (Continent) -> str

        대륙의 문자열 표현을 반환한다.
        """

        result = self.name
        for country in countries:
            result += '\n' + str(country)

        return result
