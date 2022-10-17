"""
    To declare Variable as:
        Public syntax:
            variable name
        private syntax:
            __variable name # use double underscore -> __ <-
        protected syntax:
            _variable name  # use single underscore -> _ <-
    # anything within class is considered as a public member if not set.
    
"""

# class-keyword class_name
class Student:
    """ declaration of variable at class level which will not get initialized 
        when constructor/object is created """ 
    school_name = "CDAC"    


    """ declaration of variable at class level which will get initialized 
        when constructor/object is created """

# public builtin function which get executed when object is created
    def __init__(self,rcv_name,rcv_rollno,rcv_pocket_money,rcv_course) -> None:
        self.student_name = rcv_name
        self.student_rollno = rcv_rollno
        self._student_pocket_money = rcv_pocket_money
        self.__student_enrolled_coursename = rcv_course

# public function which returns private parameter of a particular object 
    def get_enrolled_course(self):
        return self.__student_enrolled_coursename

# public function which returns protected parameter of a particular object 
    def get_student_pocket_money(self):
        return self._student_pocket_money

# public function which update private parameter of a particular object 
    def enroll(self,rcv_course_name): 
            # self-> object, rcv_course_name-> recieved parameter
        self.__student_enrolled_coursename = rcv_course_name
        
# public function which update private parameter of a particular object 
    def unenroll(self):
        self.__student_enrolled_coursename = None

# public function which update private parameter of a class 
    @classmethod    #-> decorator
    def change_schoolname(cls,rcv_schoolname):
        cls.school_name = rcv_schoolname

# ---------------- End of class --------------------------------

# -------------- main func ----------------------------
def main():
# Creating an object of class also called as constructor
    gaurav = Student("Gaurav",1,100,'Python')
                    #^ Paramateres to be updated for a particular object
    pratik = Student("Pratik",2,100,'Python')
# Accessing public parameters directly
    print(gaurav.student_name)

# Accessing private parameters using public function
    print(gaurav.get_student_pocket_money())


    print("Before Enroll call ", gaurav.get_enrolled_course())

# Updating private parameters using public function
    gaurav.enroll("Scala")
    print("After Enroll call ", gaurav.get_enrolled_course())

    print("Before change  ", gaurav.school_name)
    print("Before change  ", pratik.school_name)

# Updating private parameters using public function
    Student.change_schoolname("Sunbeam")
#^ this will change values of every objects

    print("After change  ", gaurav.school_name)
    print("After change  ", pratik.school_name)

    gaurav.school_name = "SPPU"
#^ this will change values of a particular object

    print("After update  ", gaurav.school_name)
    print("After update  ", pratik.school_name)


main()      # calling main func 
