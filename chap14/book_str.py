class Book:
    ... 이전 코드 참고 ...

    def __str__(self):
        """ (Book) -> str

        이 책에 대한 읽기 편한 표현을 반환한다. 
        """

        return """Title: {0}
Authors: {1}
Publisher: {2}
ISBN: {3}""".format(
    self.title, ', '.join(self.authors), self.publisher, self.ISBN)

if __name__ == '__main__':
    pybook = Book("Practical Programming",
        ["Campbell", "Gries", "Montojo"],
        "Pragmatic Bookshelf",
        "978-1-6805026-8-8")
    print(pybook)
