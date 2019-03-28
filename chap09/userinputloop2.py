text = ""
while text != "quit": 
    text = input("화학식을 입력하세요 (종료하려면 'quit'): ")
    if text == "quit":
        print("프로그램을 종료합니다.") 
    elif text == "H2O": 
        print("물")
    elif text == "NH3": 
        print("암모니아")
    elif text == "CH4": 
        print("메탄")
    else: 
        print("알 수 없는 화합물")