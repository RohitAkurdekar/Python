"""
    Types of sequenece DT are:
    1.Strings
    2.List
    3.Tuples
# mystring[start=0:stop=(n-1):slice=1]
"""
"""
# String
my_seq_var ="ROHIT"

#List
# my_seq_var =['R','O','H','I','T']

#Tuple
# my_seq_var =('R','O','H','I','T')

# Index access
print("-------- Index access -----------------")
print("0: ",my_seq_var[0])
print("2: ",my_seq_var[2])
print("4: ",my_seq_var[4])
print()

# slicing
print("-------- Slicing -----------------")
print(" :    ",my_seq_var[:])
print("2:    ",my_seq_var[2:])
print(" :3:1 ",my_seq_var[:3:1])
print(" :3:2 ",my_seq_var[:3:2])
print("2:3:1 ",       my_seq_var[      2:3:1 ])
print("slice(2,3,1) ",my_seq_var[slice(2,3,1)])
print("slice(3) ",my_seq_var[slice(3)])
print()
"""
number = range(5)

for i in number:
    print(i,end='\t')
print()

