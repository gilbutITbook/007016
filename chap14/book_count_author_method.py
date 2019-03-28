class Book:
    """제목과 저자 목록, 출판사, ISBN, 가격을 포함하는 책 정보
    """

    def num_authors(self):
        """ (Book) -> int

        이 책의 저자수를 반환한다. 

        >>> pybook = Book()
        >>> pybook.authors = ["Campbell", "Gries", "Montojo"]
        >>> pybook.num_authors()
        3
        """

        return len(self.authors)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
