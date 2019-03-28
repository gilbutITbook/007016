>>> s = 'C3H7'
>>> total = 0 # 지금까지 본 수의 합
>>> count = 0 # 지금까지 본 수의 개수
>>> for i in range(len(s)):
...     if s[i].isalpha():
...         continue
...     total = total + int(s[i])
...     count = count + 1
...
>>> total
10
>>> count
2
