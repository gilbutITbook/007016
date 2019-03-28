class Rectangle(object):
    """이미지의 직사각형 영역을 표현하는 클래스"""

    def __init__(self, x0, y0, x1, y1):
        """ (Rectangle, int, int, int, int) -> NoneType

        넓이가 0이 아닌 직사각형을 생성합니다. 
        (x0,y0)는 왼쪽 하단 좌표입니다.
        (x1,y1)은 오른쪽 상단 좌표입니다.
        """

        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1

    def area(self):
        """ (Rectangle) -> number

       직사각형의 넓이(area)를 반환한다.
        """

        return (self.x1 - self.x0) * (self.y1 - self.y0)

    def contains(self, x, y):
        """ (Rectangle, int, int) -> bool

        점 (x,y)가 직사각형 안에 포함되면 True,
        아니면 False를 반환한다
        """

        return (self.x0 <= x <= self.x1) and \
               (self.y0 <= y <= self.y1)
