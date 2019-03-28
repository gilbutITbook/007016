import time
import random
from sorts import selection_sort
from sorts import insertion_sort
from sorts import mergesort


def built_in(L):
    """ (list) -> NoneType
    list.sort를 호출한다. 사용자가 작성한 정렬 함수와 똑같이 처리하려면 
    list.sort를 호출할 사용자 정의 함수가 있어야 한다.
    """
    
    L.sort()


def print_times(L):
    """ (list) -> NoneType

    선택 정렬과 삽입 정렬, list.sort를 실행하는 데 걸린 밀리초를 출력한다.
    """

    print(len(L), end='\t')
    for func in (selection_sort, insertion_sort, mergesort, built_in):
        if func in (selection_sort, insertion_sort) and len(L) > 10000:
            continue

        L_copy = L[:]
        t1 = time.perf_counter()
        func(L_copy)
        t2 = time.perf_counter()
        print("{0:7.1f}".format((t2 - t1) * 1000.), end='\t')
    print()  # 새 줄을 출력한다. 

for list_size in [10, 1000, 2000, 3000, 4000, 5000, 10000]:
    L = list(range(list_size))
    random.shuffle(L)
    print_times(L)
