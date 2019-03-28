>>> def is_positive(x: float) -> bool:
...     """x가 양수면 True를 반환합니다(Return True iff x is positive).
... 
...     >>> is_positive(3) 
...     True  
...     >>> is_positive(-4.6) 
...     False  
...     """  
...     returnx>0 
...
>>> is_positive(3) 
True  
>>> is_positive(-4.6) 
False
>>> is_positive(0) 
False 