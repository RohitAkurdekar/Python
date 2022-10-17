
#Hybrid Inheritance
# When inheritance is consists of multiple types or a combination of different inheritance is called hybrid inheritance

# Parent class
class Vehicle:
    def vehicle_info(self):
        print("Inside Vehicle class")

# Child class
class Car(Vehicle):
    def car_info(self):
        print("Inside Car class")

# Child class
class Truck(Vehicle):
    def truck_info(self):
        print("Inside Truck class")

# Child class
# Sports Car can inherits properties of Vehicle and Car
class SportsCar(Car, Vehicle):
    def sports_car_info(self):
        print("Inside SportsCar class")

# hybrid inheritence
def Hybrid():
    # create object
    s_car = SportsCar()

    s_car.vehicle_info()
    s_car.car_info()
    s_car.sports_car_info()
