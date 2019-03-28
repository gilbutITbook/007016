import time

t1 = time.perf_counter()

# 시간을 측정할 코드는 여기에 넣습니다.

t2 = time.perf_counter()
print('The code took {:.2f}ms'.format((t2 - t1) * 1000.))
