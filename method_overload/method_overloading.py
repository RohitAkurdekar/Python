# Method Overloading
# The process of calling the same method with different parameters is known as method overloading.
# Python does not support method overloading. 

class Calc:
    # func gets ignored
    def addition(self,a, b):
        c = a + b
        print(c)
    # func gets executed
    def addition(self,a, b, c):
        d = a + b + c
        print(d)
# object creation
obj1 = Calc()
# the below line shows an error
try:
    obj1.addition(4, 5)
except:
    print("Error aali........")

# This line will call the second product method
obj1.addition(3, 7, 5)

