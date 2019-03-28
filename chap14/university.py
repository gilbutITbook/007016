class Member:
    """ 대학에 소속된 사람 """ 

    def __init__(self, name: str, address: str, email: str) -> None:
        """이름과 집 주소, 이메일 주소로 새로운 소속원을 생성한다.
        """

        self.name = name
        self.address = address
        self.email = email

class Faculty(Member):
    """ 대학교수 """ 

    def __init__(self, name: str, address: str, email: str,
                 faculty_num: str) -> None:
       """이름과 집 주소, 이메일 주소, 교직원 번호(faculty_num), 
        빈 과목 목록으로 새로운 교수를 생성한다.
        """

        super().__init__(name, address, email)
        self.faculty_number = faculty_num
        self.courses_teaching = []


class Student(Member):
    """ 대학생 """ 

    def __init__(self, name: str, address: str, email: str,
                 student_num: str) -> None:
        """이름과 집 주소, 이메일 주소, 학번(student_num), 빈 수강했던 과목 목록, 
        빈 수강 중인 과목 목록으로 새로운 학생을 생성한다.
        """

        super().__init__(name, address, email)
        self.student_number = student_num
        self.courses_taken = []
        self.courses_taking = []
