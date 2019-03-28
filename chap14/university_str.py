class Member:
    """ 대학에 소속된 사람 """ 

    def __init__(self, name: str, address: str, email: str) -> None:
        """이름과 집 주소, 이메일 주소로 새로운 소속원을 생성한다.
        """

        self.name = name
        self.address = address
        self.email = email

    def __str__(self) -> str:
        """이 소속원의 문자열 표현을 반환한다. 

        >>> member = Member('Paul', 'Ajax', 'pgries@cs.toronto.edu')
        >>> member.__str__()
        'Paul\\nAjax\\npgries@cs.toronto.edu'
        """

        return '{}\n{}\n{}'.format(self.name, self.address, self.email)


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

    def __str__(self) -> str:
        """이 교수의 문자열 표현을 반환한다. 

        >>> faculty = Faculty('Paul', 'Ajax', 'pgries@cs.toronto.edu', '1234')
        >>> faculty.__str__()
        'Paul\\nAjax\\npgries@cs.toronto.edu\\n1234\\nCourses: '
        """

        member_string = super().__str__()

        return '''{}\n{}\nCourses: {}'''.format(
            member_string,
            self.faculty_number,
            ' '.join(self.courses_teaching))


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

if __name__ == "__main__":
    f = Faculty('Paul', 'Ajax', 'pgries@cs.toronto.edu', '1234')
    print(f)
    import doctest
    doctest.testmod()
