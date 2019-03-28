# 다가(multivalued) 할당문으로 제어값 설정
time, population, growth_rate = 0, 1000, 0.21

# 원래 수의 정확히 두 배일 때까지 멈추지 않는다.
while population != 2000:
    population = population + growth_rate * population
    print(round(population))
    time = time + 1

print("박테리아가 두 배가 되는 데", time, "분이 걸렸습니다.")
