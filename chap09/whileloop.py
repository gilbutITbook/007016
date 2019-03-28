time = 0
population = 1000 # 처음에는 1000개 박테리아로 시작 
growth_rate = 0.21 # 분당 21% 성장
while population < 2000:
    population = population + growth_rate * population
    print(round(population))
    time = time + 1
	
print("It took", time, "minutes for the bacteria to double.")
print("The final population was", round(population), "bacteria.")
