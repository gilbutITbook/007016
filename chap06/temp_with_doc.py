"""온도를 다루는 함수"""

def to_celsius(t):
    """화씨를 섭씨로 변환합니다."""
    return round((t - 32.0) * 5.0 / 9.0)

def above_freezing(t):
    """온도가 섭씨로 어는점보다 높으면 True, 낮으면 False를 반환한다."""
    return t > 0
