"""
1) Lets create a student list named "members" with following names in it

Pratiksha,Kevin,Sachin,Yuvraj,Sania

Do the following operations on the created list 
 (i) Display number of elements in the members list
 (ii) Add "Ross" to the members collection 
 (iii) Add "David","Bret","Sanju"  to the members collection 
 (iv) Remove the third member from the collection 
 (v) Remove the last member from the collection 
 ( vi)  Display third, fourth and fifth element from the collection 
 

members = ["Pratiksha", "Kevin", "Sachin", "Yuvraj", "Sania"]

print("Total number of members",len(members))
members.append("Ross")
print(members)
members.extend(["David","Bret","Sanju"])
print(members)
members.pop(3)
print(members)
members.pop((len(members)-1))
print(members)
print(members[3:6:1])

"""
"""

2) Lets create a dictionary named "Capitals" of country and their capitals 

India : New Delhi
USA : Washington DC
Nepal: Kathmandu
Ukraine : Kyiv

Do the following operations on the created dictionary
 (i) Display number of elements in the Capitals collection
 (ii) Add Afghanistan: Kabul  to the Capitals collection 
 (iii) Add "Albania	Tirana
			Algeria	Algiers
			Andorra	Andorra la Vella
			to the Capitals collection 
 (iv) Remove the USA from the collection 



Capitals = {"India":"New Delhi",
            "USA" : "Washington DC",
            "Nepal": "Kathmandu",
            "Ukraine" : "Kyiv"}

print("Number of elements in Capitals are ",len(Capitals))
print("----------------------------------------------------")
Capitals["Afghanistan"] = "Kabul"
print(Capitals)
print("----------------------------------------------------")
Capitals.update({"Albania":	"Tirana",
			"Algeria":	"Algiers",
			"Andorra":	"Andorra la Vella"})
print(Capitals)
print("----------------------------------------------------")
Capitals.pop("USA")
print(Capitals)
"""
"""

3) Take a number from the user and print fibonacci sequence till that number 
    USING Range Iterator 
	eg : fibonnaci sequence for 5 is 1,2,3,5

print("----------------------------------------------------")

my_number = int(input("Enter a number: "))

# ---------------------- Fibbonacci series ---------------------------
oldValue = 0
newValue = 1
print(oldValue,end='\t')
print(newValue,end='\t')
for i in range(my_number):
    temp = oldValue         # store old value in temp
    oldValue = newValue     # Update old value by new value
    newValue+=temp          # Add old value i.e temp in new value
    
    if (newValue > my_number):   # break if new value reaches
        break

    print(newValue,end='\t')    # print new value
print()
print("----------------------------------------------------")

"""
"""

4) Create two sets as follows 

A = 1,2,3,4,5
B = 18,19,20,21

Perform following operations on these :
a) Union
b) Intersection 
c) A-B
d) B-A

Display if 20 is a member of set B 

Do the following operations on the created set A	 
 (i) Display number of elements in the set A
 (ii) Add 365 to the set
 (iii) Add 12,13,14  to set B
 (iv) Remove 12 from set B


print("----------------------------------------------------")

A = {1,2,3,4,5,6,7}
B = {6,7,18,19,20,21}

print("Union of A and B :",A|B)
print("Intersection of A and B :",A&B)
print("A - B :",A-B)
print("B - A :",B-A)
print("----------------------------------------------------")

print("number of elements in the set A are ",len(A))
A.add(365)
print("A: ",A)
B.update(range(12,15,1))
print("B: ",B)
B.remove(12)
print("B: ",B)
print("----------------------------------------------------")
"""
"""
5)  create a function named factorial() that takes in a number and 
    displays the factorial of that number

print("----------------------------------------------------")
def Factorial(number:int)->int:
    fact = 1
    for i in range(number,1,-1):
        fact = fact*i
    return fact

my_number = int(input("Enter a number: "))

print("Factorial of",my_number,"is",Factorial(my_number))
print("----------------------------------------------------")
"""
"""
6) create a function that  take a number from the user and 
    returns a list of  even numbers from 1 to that number   

print("----------------------------------------------------")
def evenList(number):
    my_list = []
    for i in range(1,number+1):
        if i%2==0:
            my_list.append(i)
    return my_list

my_number = int(input("Enter a number: "))
print("Even number till ",my_number,"are",evenList(my_number))
print("----------------------------------------------------")
"""
"""
7) create a function that takes in a number from the user and 
    returns a tuple of all Odd numbers from 1 to that number 


print("----------------------------------------------------")
def oddList(number):
    my_list = ()
    for i in range(1,number+1):
        if i%2!=0:
            temp = (i,)
            my_list = my_list+temp
            
    return my_list

my_number = int(input("Enter a number: "))
print("ODD number till ",my_number,"are",oddList(my_number))
print("----------------------------------------------------")

"""
"""
8) create a lambda function take a number from the user and 
    print all prime numbers from 1 to that number 


# CAN NOT USE LAMBDA FUNCTION TO IMPLEMENT MULTI LINE FUNCTION
"""



