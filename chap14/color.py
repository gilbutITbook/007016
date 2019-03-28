class Color(object):
    """RGB 색상, 빨강, 녹색, 파란색 요소."""

    def __init__(self, r, g, b):
        """빨강 값 r, 녹색 값 g, 파랑 값 b로 된 새 색상.
        모든 구성 요소는 정수 범위 0~255를 갖는다."""

        self.red = r
        self.green = g
        self.blue = b
