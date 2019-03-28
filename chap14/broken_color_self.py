class Color(object):
    """RGB 색상, 빨강, 녹색, 파란색 요소."""
    
    def lightness(self):
        """이 색상의 밝기를 반환한다."""
        # 실패: 'red', 'green', 'blue' 변수가 없다
        strongest = max(red, green, blue)
        weakest   = min(red, green, blue)
        return 0.5 * (strongest + weakest) / 255
