#Method Resolution Order in Python
#In Python, Method Resolution Order(MRO) is the order by which Python looks for a method or attribute

#parent class
class A:
    def process(self):
        print(" In class A")

# child class
class B(A):
    def process(self):
        print(" In class B")

#child class
class C(B, A):
    def process(self):
        print(" In class C")

# Method resolution order
def M_R_O():
    # Creating object of C class
    C1 = C()
    C1.process()
    print(C.mro())
