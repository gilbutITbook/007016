>>> def get_weekday(current_weekday: int, days_ahead: int) -> int:
...     """current_weekday에서 days_ahead만큼 지나면
...     무슨 요일인지 반환합니다.
...
...     current_weekday는 현재 요일로서 범위는 1부터 7까지이며, 
...     오늘이 일요일(1)인지, 월요일(2)인지, 토요일(7)인지 등을 나타냅니다. 
...
...     days_ahead는 오늘부터 며칠 후인지 뜻합니다.
...
...     >>> get_weekday(3, 1)
...     4
...     >>> get_weekday(6, 1)
...     7
...     >>> get_weekday(7, 1)
...     1
...     >>> get_weekday(1, 0)
...     1
...     >>> get_weekday(4, 7)
...     4
...     >>> get_weekday(7, 72)
...     2
...     """
...     return (current_weekday + days_ahead) % 7
...

>>> def days_difference(day1: int, day2: int) -> int:
...     """ day1과 day2 간 날짜수 차이를 반환합니다. 
...     이때 day1과 day2는 (그해의 몇 번째 날인지 가리키는) 
...     1에서 365 사이 값입니다.
...
...     >>> days_difference(200, 224)
...     24
...     >>> days_difference(50, 50)
...     0
...     >>> days_difference(100, 99)
...     -1
...     """
...     return day2 - day1
...
>>> days_difference(200, 224)
24
>>> days_difference(50, 50)
0
>>> days_difference(100, 99)
-1

>>> def get_birthday_weekday(current_weekday: int, current_day: int,
...                          birthday_day: int) -> int:
...     """ 요일은 current_weekday, 그해의 몇 번째 날인지는 current_day일 때,
...     birthday_day가 무슨 요일인지 반환합니다.
...
...     current_weekday는 현재 요일로서 범위는 1부터 7까지이며, 
...     오늘이 일요일(1)인지, 월요일(2)인지, 토요일(7)인지 등을 나타냅니다. 
...
...     current_day와 birthday_day는 1부터 365 사이의 값입니다.
...
...     >>> get_birthday_weekday(5, 3, 4)
...     6
...     >>> get_birthday_weekday(5, 3, 116)
...     6
...     >>> get_birthday_weekday(6, 116, 3)
...     5
...     """
...     days_diff = days_difference(current_day, birthday_day)
...     return get_weekday(current_weekday, days_diff)
...
