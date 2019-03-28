class Book:
    """제목과 저자 목록, 출판사, ISBN, 가격을 포함하는 책 정보
    """

    def __init__(self, title, authors, publisher, isbn, price):
        """ (Book, str, list of str, str, str, number) -> NoneType

        제목이 title이고, 작성한 저자는 authors고, 출판사는 publisher고, 
        isbn은 ISBN이고, 가격은 price 달러인 새 책을 생성한다.

        >>> python_book = Book( \
                'Practical Programming', \
                ['Campbell', 'Gries', 'Montojo'], \
                'Pragmatic Bookshelf', \
                '978-1-6805026-8-8', \
                25.0)
        >>> python_book.title
        'Practical Programming'
        >>> python_book.authors
        ['Campbell', 'Gries', 'Montojo']
        >>> python_book.publisher
        'Pragmatic Bookshelf'
        >>> python_book.isbn
        '978-1-6805026-8-8'
        >>> python_book.price
        25.0
        """

        self.title = title
        # 호출자가 나중에 리스트를 수정할 경우를 대비해서 저자 리스트를 복사한다.
        self.authors = authors[:]
        self.publisher = publisher
        self.ISBN = isbn
        self.price = price

    def num_authors(self):
        """ (Book) -> int

        이 책의 저자수를 반환한다. 

        >>> python_book = Book( \
                'Practical Programming', \
                ['Campbell', 'Gries', 'Montojo'], \
                'Pragmatic Bookshelf', \
                '978-1-6805026-8-8', \
                25.0)
        >>> pybook.num_authors()
        3
        """

        return len(self.authors)

    def __str__(self):
        """ (Book) -> str

        이 책에 대한 읽기 편한 표현을 반환한다.
        """

        return """Title: {0}
Authors: {1}
Publisher: {2}
ISBN: {3}
Price: ${4}""".format(
    self.title, ', '.join(self.authors), self.publisher, self.ISBN,
    self.price)

if __name__ == '__main__':

    python_book = Book(
        'Practical Programming',
        ['Campbell', 'Gries', 'Montojo'],
        'Pragmatic Bookshelf',
        '978-1-6805026-8-8',
        25.0)

    survival_book = Book(
        "New Programmer's Survival Manual",
        ['Carter'],
        'Pragmatic Bookshelf',
        '978-1-93435-681-4',
        19.0)

    print('{0} was written by {1} authors and costs ${2}'.format(
        python_book.title, python_book.num_authors(), python_book.price))

    print('{0} was written by {1} authors and costs ${2}'.format(
        survival_book.title, survival_book.num_authors(), survival_book.price))
