"""
# Single inheritance 
# Base class
class Vehicle:
    def Vehicle_info(self):
        print('Inside Vehicle class')
# Child class
class Car(Vehicle):
    def car_info(self):
        print('Inside Car class')

# Create object of Car
car = Car()

# access Vehicle's info using car object
car.Vehicle_info()
car.car_info()


# multiple inheritance example
# Parent class 1
class Person:
    def person_info(self, name, age):
        print('Inside Person class')
        print('Name:', name, 'Age:', age)

# Parent class 2
class Company:
    def company_info(self, company_name, location):
        print('Inside Company class')
        print('Name:', company_name, 'location:', location)

# Child class
class Employee(Person, Company):
    def Employee_info(self, salary, skill):
        print('Inside Employee class')
        print('Salary:', salary, 'Skill:', skill)

# Create object of Employee
emp = Employee()

# access data
emp.person_info('Jessa', 28)
emp.company_info('Google', 'Atlanta')
emp.Employee_info(12000, 'Machine Learning')


# Multilevel Inheritance example
# Base class
class Vehicle:
    def Vehicle_info(self):
        print('Inside Vehicle class')

# Child class
class Car(Vehicle):
    def car_info(self):
        print('Inside Car class')

# Child class
class SportsCar(Car):
    def sports_car_info(self):
        print('Inside SportsCar class')

# Create object of SportsCar
s_car = SportsCar()

# access Vehicle's and Car info using SportsCar object
s_car.Vehicle_info()
s_car.car_info()
s_car.sports_car_info()


#Hierarchical Inheritance
# In Hierarchical inheritance, more than one child class is derived from a single parent class. In other words, we can say one parent class and multiple child classes.

class Vehicle:
    def info(self):
        print("This is Vehicle")

class Car(Vehicle):
    def car_info(self, name):
        print("Car name is:", name)

class Truck(Vehicle):
    def truck_info(self, name):
        print("Truck name is:", name)

obj1 = Car()
obj1.info()
obj1.car_info('BMW')

obj2 = Truck()
obj2.info()
obj2.truck_info('Ford')


#Hybrid Inheritance
# When inheritance is consists of multiple types or a combination of different inheritance is called hybrid inheritance

class Vehicle:
    def vehicle_info(self):
        print("Inside Vehicle class")

class Car(Vehicle):
    def car_info(self):
        print("Inside Car class")

class Truck(Vehicle):
    def truck_info(self):
        print("Inside Truck class")

# Sports Car can inherits properties of Vehicle and Car
class SportsCar(Car, Vehicle):
    def sports_car_info(self):
        print("Inside SportsCar class")

# create object
s_car = SportsCar()

s_car.vehicle_info()
s_car.car_info()
s_car.sports_car_info()


#Python super() function
#When a class inherits all properties and behavior from the parent class is called inheritance. 
# In such a case, the inherited class is a subclass and the latter class is the parent class.

#In child class, we can refer to parent class by using the super() function. 
# The super function returns a temporary object of the parent class that allows us to call a parent class method inside a child class method

class Company:
    def company_name(self):
        return 'Google'

class Employee(Company):
    def info(self):
        # Calling the superclass method using super()function
        c_name = super().company_name()
        print("Jessa works at", c_name)

# Creating object of child class
emp = Employee()
emp.info()


#Method Overriding
#In inheritance, all members available in the parent class are by default available in the child class.
#  If the child class does not satisfy with parent class implementation,
# then the child class is allowed to redefine that method by extending additional functions in the child class.
#  This concept is called method overriding.

class Vehicle:
    def max_speed(self):
        print("max speed is 100 Km/Hour")

class Car(Vehicle):
    # overridden the implementation of Vehicle class
    def max_speed(self):
        print("max speed is 200 Km/Hour")

# Creating object of Car class
car = Car()
car.max_speed()


#Method Resolution Order in Python
#In Python, Method Resolution Order(MRO) is the order by which Python looks for a method or attribute

class A:
    def process(self):
        print(" In class A")

class B(A):
    def process(self):
        print(" In class B")

class C(B, A):
    def process(self):
        print(" In class C")

# Creating object of C class
C1 = C()
C1.process()
print(C.mro())


# What is Polymorphism in Python?
# Polymorphism in Python is the ability of an object to take many forms.
#  In simple words, polymorphism allows us to perform the same action in many different ways.

students = ['Emma', 'Jessa', 'Kelly']
school = 'ABC School'

# calculate count
print(len(students))
print(len(school))

"""

#Method Overloading
#The process of calling the same method with different parameters is known as method overloading.
#  Python does not support method overloading. 

class Calc:
    def addition(self,a, b):
        c = a + b
        print(c)

    def addition(self,a, b, c):
        d = a + b + c
        print(d)

obj1 = Calc()
# the below line shows an error
obj1.addition(4, 5)

# This line will call the second product method
obj1.addition(3, 7, 5)



