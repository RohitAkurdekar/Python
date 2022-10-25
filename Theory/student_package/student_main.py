from Student import Student

# main function
print("I am in main")

# creating an object of Student class 
gaurav= Student("Gaurav",1,100,'Python')

# accessing the instance attribute using . notation since it is public
print(gaurav.student_name)


# invoking the instance method using . notation since it is public    
print(gaurav.get_student_pocket_money())

print("Before Enroll call ", gaurav.get_enrolled_course())
# changing the instance variable using instance method
gaurav.enroll("Scala")
print("After Enroll call ", gaurav.get_enrolled_course())

pratik= Student("Pratik",2,200,'Java')
print(gaurav.student_name)
print(gaurav.get_student_pocket_money())
print("Before Enroll call ", gaurav.get_enrolled_course())
gaurav.enroll("C")
print("After Enroll call ", gaurav.get_enrolled_course())


# accessing the class variable using instance object reference 
print("School name is",gaurav.school_name)
# changing the class variable using class method 
Student.change_schoolname("Sunbeam")
print("Gaurav School name is",gaurav.school_name)
print("Pratik School name is",pratik.school_name)
