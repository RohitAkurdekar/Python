"""

"""
import calendar 


name = input("Enter name of student: ")
age = int(input("Enter age of student: "))
rollno = int(input("Enter roll no: "))
DoB = (input("Enter birth date in DD/MM/YYYY format: "))
FavSub = input("Enter favourite subject: ")
FavSubMarks = int(input("Enter marks of subject: "))
totlaMarks = int(input("Enter total marks: "))

def camelcase(list_words):  
    converted = "".join(word[0].upper() + word[1:].lower() for word in list_words)  
    return converted[0].lower() + converted[1:]  

arrDoB = DoB.split('/')

print("------------------------------------------------")
print("Sentence case: ",name.capitalize())
print("Camel case   : ",camelcase(name.split(" ")))
print("Sentence case: ",name.lower())
print("Sentence case: ",name.upper())
print("------------------------------------------------")
print("Year born: ",arrDoB[2])
print("Day born: ",calendar.day_name[calendar.weekday(int(arrDoB[2]),int(arrDoB[1]),int(arrDoB[0]))])
print("------------------------------------------------")
print("Percentage: ",round(FavSubMarks/totlaMarks*100,2))
print("------------------------------------------------")
print("Welcome Mr/Ms ",name," to the world of programming, It will fun to be here\
 You could use your fav sub ",FavSub,"to your advantage here")
print("------------------------------------------------")