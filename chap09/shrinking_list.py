from typing import List

def remove_neg(num_list: List[float]) -> None: 
    """리스트 num_list에서 음수를 삭제한다.
    
    >>> numbers = [-5, 1, -3, 2]
    >>> remove_neg(numbers)
    >>> numbers
    [1, 2]
    """ 

    for item in num_list: 
        if item < 0: 
            num_list.remove(item)
              