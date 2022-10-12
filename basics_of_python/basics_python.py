# Basics of python
# Syntax to run python file --> python -u filename.py 

import string

"""
    Accept two numbers from the user and print
    1. arithmetic ops
    2. square of a number
    3. num1 raised to num2
"""


num1 = int(input("Enter n1: "))
num2 = int(input("Enter n2: "))
print("------------------------------------------------------------")
print(num1,"+",num2,"=",num1+num2)
print(num1,"-",num2,"=",num1-num2)
print(num1,"*",num2,"=",num1*num2)
print(num1,"/",num2,"=",num1/num2)
print("square of ",num2, " is ",num2*num2)
print(num1,"^",num2 , " is ",pow(num1,num2))
print("------------------------------------------------------------")

"""
    Accept a string from user and print it in UPPERCASE
"""
str1 = input("Enter a string: ")
print(str1," --> ",str1.upper())
print("------------------------------------------------------------")

"""
    Take a name,%salary increment and salary, display incremented salary
"""
emp_name = input("Enter name of employee: ")
basic_salary = int(input("Enter basic salary : "))
raise_by_perc = int(input("Enter % to be incremented: "))
print("-----------------------------")
print("Name of employee :",emp_name)
print("Basic salary     :",basic_salary)
print("Increment by     :",basic_salary*raise_by_perc/100)
print("-----------------------------")
print("Final salary     :",basic_salary + basic_salary*raise_by_perc/100)
print("------------------------------------------------------------")


"""
    Get the height from the user in cms and display the user height back to console
    in foot/feet and inches
"""

height_cm = int(input("Enter height in cms:"))
height_feet = height_cm/30.48
print("Height in feet: %.2f"%height_feet)
print("------------------------------------------------------------")


"""
    Get the no of the dollars from the user apply the conversion of 
    1 dollar = 82 rupees and print the amount to the console in rupees
"""

usd = int(input("Enter amount in $"))
print("INR: ",82*usd)
print("------------------------------------------------------------")


"""
    Take the source, destination, fare in INR, discount_rate percentage 
    from the user and display the string 
    ex: "fare from mumbai to pune is 300 INR with has a discount of 5%
"""

source = input("Enter name of a Source: ")
destination = input("Enter name of a Destination: ")
INR = int(input("Enter fare amount: "))
discount = int(input("Enter discount given: "))
print("Fare from ",source," to ",destination," is ",INR," with has a discount of ",discount,"%")
print("------------------------------------------------------------")
