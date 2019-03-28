class Book:
    ...이전 코드 참고...

    def __eq__(self, other):
        """이것은 __eq__를 정의하는 잘못된 방법이다."""

        self.ISBN = other.ISBN
        return self.ISBN == other.ISBN
