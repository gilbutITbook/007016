class Book:
    """책에 관한 정보"""

    def num_authors(self) -> int:
        """이 책의 저자수를 반환한다.
        """

        return len(self.authors)
