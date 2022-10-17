
#Method Overriding
#In inheritance, all members available in the parent class are by default available in the child class.
#  If the child class does not satisfy with parent class implementation,
# then the child class is allowed to redefine that method by extending additional functions in the child class.
#  This concept is called method overriding.

# parent class
class Vehicle:
    def max_speed(self):
        print("max speed is 100 Km/Hour")

# Child class
class Car(Vehicle):
    # overridden the implementation of Vehicle class
    def max_speed(self):
        print("max speed is 200 Km/Hour")

def method_override():
    # Creating object of Car class
    car = Car()
    car.max_speed()
