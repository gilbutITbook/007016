class Color(object):
    """RGB 색상, 빨강, 녹색, 파란색 요소."""

    def lightness(self):
        """이 색상의 밝기를 계산한다."""

        strongest = max(self.red, self.green, self.blue)
        weakest   = min(self.red, self.green, self.blue)
        return 0.5 * (strongest + weakest) / 255
