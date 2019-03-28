class Rectangle(object):
    """이미지의 직사각형 영역을 표현하는 클래스"""

    def __init__(self, x0, y0, x1, y1):
        # ...이전 코드 참고...

    def area(self):
        # ...이전 코드 참고...

    def contains(self, x, y):
        # ...이전 코드 참고...

    def get_min_x(self):
        """ (Rectangle) -> int

        최소 X 좌표를 반환한다.
        """

        return self.x0

    def get_min_y(self):
        """ (Rectangle) -> int

        최소 Y 좌표를 반환한다.
        """

        return self.y0

    def get_max_x(self):
        """ (Rectangle) -> int

        최대 X 좌표를 반환한다.
        """

        return self.x1

    def get_max_y(self):
        """ (Rectangle) -> int

        최대 Y 좌표를 반환한다.
        """

        return self.y1
