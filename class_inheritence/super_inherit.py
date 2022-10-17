#Python super() function
#When a class inherits all properties and behavior from the parent class is called inheritance. 
# In such a case, the inherited class is a subclass and the latter class is the parent class.

#In child class, we can refer to parent class by using the super() function. 
# The super function returns a temporary object of the parent class that allows us to call a parent class method inside a child class method

# parent class
class Company:
    def company_name(self):
        return 'Google'

# child class
class Employee(Company):
    def info(self):
        # Calling the superclass method using super()function
        c_name = super().company_name()
        print("Jessa works at", c_name)

# super inheritence
def super_inherit():
    # Creating object of child class
    emp = Employee()
    emp.info()
