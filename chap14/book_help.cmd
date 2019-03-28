>>> help(Book)
Help on class Book in module __main__:

class Book(builtins.object)
 |  Book(title, authors, publisher, isbn)
 |  
 |  제목과 저자 목록, 출판사, ISBN, 가격을 포함하는 책 정보
 |  
 |  Methods defined here:
 |  
 |  __eq__(self, other)
 |      (Book, Book) -> bool
 |      
 |      other가 책이고, 이 책과 other의 ISBN이 같으면 True를 반환한다.
 |  
 |  __init__(self, title, authors, publisher, isbn)
 |      (Book, str, list of str, str, str) -> NoneType
 |      
 |      제목이 title이고, 작성한 저자는 authors고, 출판사는 publisher고, 
 |      isbn은 ISBN이고, 가격은 price 달러인 새 책을 생성한다.
 |  
 |  __str__(self)
 |      (Book) -> str
 |      
 |      이 책에 대한 읽기 편한 표현을 반환한다.
 |  
 |  num_authors(self)
 |      (Book) -> int
 |      
 |      이 책의 저자수를 반환한다. 
 |      
 |      >>> pybook = Book("Practical Programming",             ["Campbell", "Gries", "Montojo"],             "Pragmatic Bookshelf",             "978-1-6805026-8-8")
 |      >>> pybook.num_authors()
 |      3
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |  
 |  __dict__
 |      dictionary for instance variables (if defined)
 |  
 |  __weakref__
 |      list of weak references to the object (if defined)
 |  
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |  
 |  __hash__ = None
