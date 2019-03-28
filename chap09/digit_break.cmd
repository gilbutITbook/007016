>>> s = 'C3H7'
>>> digit_index = -1 # 숫자를 찾을 때까지는 -1이다.
>>> for i in range(len(s)):
...     # 숫자를 찾았을 때
...     if s[i].isdigit():
...         digit_index = i
...         break # 루프를 종료시킨다.
...
>>> digit_index 
1 