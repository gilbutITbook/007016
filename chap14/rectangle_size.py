class Rectangle(object):
    """이미지의 직사각형 영역을 표현하는 클래스"""

    def __init__(self, x0, y0, width, height):
        """ (Rectangle, int, int, int, int) -> NoneType

        넓이가 0이 아닌 직사각형을 생성한다. 
        (x0,y0)는 왼쪽 하단 좌표입니다.
        width와 height로 X와 Y 범위를 표현한다.
        """

        self.x0 = x0
        self.y0 = y0
        self.width = width
        self.height = height

    def area(self):
        """ (Rectangle) -> int

        직사각형의 넓이(area)를 반환한다.
        """

        return self.width * self.height

    def contains(self, x, y):
        """ (Rectangle, int, int) -> bool

        점 (x,y)가 직사각형 안에 포함되면 True,
        아니면 False를 반환한다
        """

        return (self.x0 <= x) and (x <= self.x0 + self.width) and \
               (self.y0 <= y) and (y <= self.y0 + self.height)
