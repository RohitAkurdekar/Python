# Single inheritance 
# Base class
class Vehicle:
    def Vehicle_info(self):
        print('Inside Vehicle class')
# Child class
class Car(Vehicle):
    def car_info(self):
        print('Inside Car class')

def single_inherit():
    # Create object of Car
    car = Car()

    # access Vehicle's info using car object
    car.Vehicle_info()
    car.car_info()
