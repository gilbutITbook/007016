class Color(object):
    """RGB 색상, 빨강, 녹색, 파란색 요소."""

    def __init__(self, r, g, b):
        """빨강 값 r, 녹색 값 g, 파랑 값 b로 된 새 색상.
        모든 구성 요소는 정수 범위 0~255를 갖는다."""

        self.red = r
        self.green = g
        self.blue = b

    def __str__(self):
        """RGB 튜플 형태 문자열 표현을 반환한다."""

        return '(%s, %s, %s)' % (self.red, self.green, self.blue)
