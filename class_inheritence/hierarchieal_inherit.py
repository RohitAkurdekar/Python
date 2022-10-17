#Hierarchical Inheritance
# In Hierarchical inheritance, more than one child class is derived from a single parent class. In other words, we can say one parent class and multiple child classes.

# Parent class
class Vehicle:
    def info(self):
        print("This is Vehicle")

# Child class
class Car(Vehicle):
    def car_info(self, name):
        print("Car name is:", name)

# Child class
class Truck(Vehicle):
    def truck_info(self, name):
        print("Truck name is:", name)

# Hierarchical main calling
def Hierarchical():
# Object of class
    obj1 = Car()
    obj1.info()
    obj1.car_info('BMW')

# Object of class
    obj2 = Truck()
    obj2.info()
    obj2.truck_info('Ford')
