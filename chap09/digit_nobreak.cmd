>>> s = 'C3H7'
>>> digit_index = -1 # 숫자를 찾을 때까지는 -1이다.
>>> for i in range(len(s)):
...     # 아직 숫자를 못 찾았고, s[i]가 숫자일 때
...     if digit_index == -1 and s[i].isdigit():
...         digit_index = i
...
>>> digit_index 
1 