class Student:
    
    # class variable
    school_name = "CDAC"    
    
    # paramterised constructor 
    def __init__(self,rcv_name,rcv_rollno,rcv_pocket_money,rcv_course) -> None:
        # instance variables 
        self.student_name = rcv_name 
        self.student_rollno = rcv_rollno
        self._student_pocket_money = rcv_pocket_money
        self.__student_enrolled_coursename = rcv_course

    # instance methods
    def get_enrolled_course(self):
        return self.__student_enrolled_coursename

    # instance methods
    def get_student_pocket_money(self):
        return self._student_pocket_money

    # instance methods
    def enroll(self,rcv_course_name):
        self.__student_enrolled_coursename = rcv_course_name

    # instance methods
    def unenroll(self):
        self.__student_enrolled_coursename = None

    # class methods
    @classmethod
    def change_schoolname(cls,rcv_schoolname):
        cls.school_name = rcv_schoolname
