class Color(object):
    ...other definitions as before...

    def __add__(self, other_color):
        """이것은 이 메서드를 정의하는 나쁜 방법이다."""

        self.red += other_color.red
        self.green += other_color.green
        self.blue += other_color.blue
        return self
