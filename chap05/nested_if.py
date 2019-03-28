value = input('pH 농도를 입력하세요: ') 
if len(value) > 0: 
    ph = float(value)
    if ph < 7.0: 
        print(ph, "은(는) 산성입니다.") 
    elif ph > 7.0: 
        print(ph, " 은(는) 염기성입니다.") 
    else: 
    print(ph, "은(는) 중성입니다.") 
else: 
    print("pH 농도를 입력하지 않았습니다!") 