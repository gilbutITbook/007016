class Book:
    """…"""

    def __init__(self, title, authors, publisher, isbn):
        """…"""

        self.title = title
        # 호출자가 나중에 리스트를 수정할 경우를 대비해서 저자 리스트를 복사한다.
        self.authors = authors[:]
        self.publisher = publisher
        self.ISBN = isbn

    def num_authors(self):
        """…"""

        return len(self.authors)


if __name__ == '__main__':
    pybook = Book("Practical Programming",
        ["Campbell", "Gries", "Montojo"],
        "Pragmatic Bookshelf",
        "978-1-6805026-8-8")
    pybook.num_authors()
