import time
import binary_search


def time_it(search, L, v):
    """ (function, list, object) -> number
    리스트 L에서 값 v를 찾는 검색 함수에 시간이 얼마나 걸리는지 측정한다.
    """ 

    t1 = time.perf_counter()
    search(L, v)
    t2 = time.perf_counter()

    return (t2 - t1) * 1000.0


def print_times(v, L):
    """ (object, list) -> NoneType
    linear_search(v, L)을 list.index와 while 루프 선형 검색, for 루프 선형 
    검색, 센티널 검색으로 실행하는 데 걸린 밀리초를 출력한다.
    """ 

    # list.index의 실행 시간을 구한다.
    t1 = time.perf_counter()
    L.index(v)
    t2 = time.perf_counter()
    index_time = (t2 - t1) * 1000.0

    # 그 외 세 함수의 실행 시간을 구한다.
    binary_time = time_it(binary_search.binary_search, L, v)

    print("{0}\t{1:.4f}\t{2:.4f}\t{3:.2f}".format(
            v, index_time, binary_time, index_time / binary_time))

L = list(range(10000001)) # 값이 천만 개인 리스트 

print_times(10, L) # 앞쪽은 얼마나 빨리 검색하는가?
print_times(5000000, L) # 중간 즈음은 얼마나 빨리 검색하는가?
print_times(10000000, L) # 끝부분은 얼마나 빨리 검색하는가?