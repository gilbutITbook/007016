input_file = open("hopedale.txt", "r")

# 첫 번째 줄을 건너뛴다.
input_file.readline()

# 주석들을 건너뛴다.
line = input_file.readline()
while line.startswith('#'):
	line = input_file.readline()

# 이제 나머지 줄들을 처리한다.
for line in input_file:
    line = line.strip()
    print line
input_file.close()
