import temperature_program

def get_preheating_instructions(fahrenheit: float) -> str:
    """오븐의 예열 온도를 화씨와 섭씨로 알려준다.

    >>> get_preheating_instructions(500)
    'Preheat oven to 500 degrees F (260.0 degrees C).'
    """

    cels = str(temperature_program.convert_to_celsius(fahrenheit))
    fahr = str(fahrenheit)
    return '오븐을 ' + fahr + ' 화씨 ('+ cels +' 섭씨)로 예열하세요.'


fahr = float(input('조리 온도를 화씨로 입력하세요: '))
print(get_preheating_instructions(fahr))
