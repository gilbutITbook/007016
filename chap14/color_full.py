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

        return 'Color(%s, %s, %s)' % (self.red, self.green, self.blue)

    def __add__(self, other_color):
        """이 색상의 빨강, 녹색, 파랑에 
        다른 색상의 구성요소를 더해서 새 색상을 반환한다.
        합계가 255보다 크면 색상을 255로 설정한다.
        """

        return Color(min(self.red + other_color.red, 255),
                     min(self.green + other_color.green, 255),
                     min(self.blue + other_color.blue, 255))

    def __sub__(self, other_color):
        """이 색상의 빨강, 녹색, 파랑에
        다른 색상의 구성요소를 빼서 새 색상을 반환한다.
        합계가 0보다 작으면 색상을 0으로 설정한다.
        """

        return Color(max(self.red - other_color.red, 0),
                     max(self.green - other_color.green, 0),
                     max(self.blue - other_color.blue, 0))

    def __eq__(self, other_color):
        """이 색상의 구성요소와 다른 색상의 구성요소와 같으면 
        True를 반환한다.
        """

        return self.red == other_color.red and self.green == \
            other_color.green and self.blue == other_color.blue

