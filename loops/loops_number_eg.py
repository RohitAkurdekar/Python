"""
-----------------------
Loops and Conditionals 
----------------------
# Solve the following using either while/do while loops
1) Take a number from the user and print sum from 1 to that number 
2) Take a number from the user and print all prime numbers from 1 to that number 
3) Take a number from the user and print all Odd numbers from 1 to that number 
4) Take a number from the user and print all Even numbers from 1 to that number 
5) Take a number from the user and print fibonacci sequence till that number
	eg : fibonnaci sequence for 5 is 1,2,3,5

"""


num1 = int(input("\nEnter a number: "))
sum=0
value=0

# loop till value is less than number
while True:
    sum+=value          # add value in previous sum
    if value==num1:     # break if loop exceeds
        break
    else:
        value+=1        # increment value

print("\nSum of a numbers from 1 to",num1,"are : ",sum)
print("\n------------ End Of sum upto given number ---------------------")

# ---------------------- Prime numbers ---------------------------
print("\Prime numbers upto",num1,"are: \n")
value=2
# To loop from 2 to num1
while True:
    if value>num1:  # break if loop exceeds
        break
    # Logic for prime number
    elif(value>1):  # loop from 2 to value
        divisor=2
        while True:
            if (value%divisor==0):    # condition for prime number
                break
            else:
                divisor+=1       # if remainder is not 0 then increment divisor
        if (divisor==value):
            print(value,end='\t') # print prime value 
    else:
        print(value,end='\t')     # print value if value is <= 1
    value+=1            # Increment value

print("\n------------ End Of Prime Number upto given number ---------------------")

# ---------------------- EVEN numbers ---------------------------

value=1
print("\nEven numbers upto",num1,"are:")
# To loop from 1 to num1
while True:
    if value>num1:  # break if loop exceeds
        break
    # Logic for prime number
    else:  # loop from 2 to value
        if (value%2==0):
            print(value,end='\t')
    value+=1            # Increment value

print("\n------------ End Of Even Numbers upto given number ---------------------")

# ---------------------- ODD numbers ---------------------------
value=1
print("\nODD numbers upto",num1,"are:")
# To loop from 1 to num1
while True:
    if value>num1:  # break if loop exceeds
        break
    # Logic for prime number
    else:  # loop from 2 to value
        if (value%2!=0):
            print(value,end='\t')
    value+=1            # Increment value

print("\n------------ End Of ODD Numbers upto given number ---------------------")

# ---------------------- Fibbonacci series ---------------------------
oldValue = 0
newValue = 1
print(oldValue,end='\t')
print(newValue,end='\t')
# loop till series reaches given number
while True:
    temp = oldValue         # store old value in temp
    oldValue = newValue     # Update old value by new value
    newValue+=temp          # Add old value i.e temp in new value
    
    print(newValue,end='\t')    # print new value

    if (newValue > num1):   # break if new value reaches
        break
    
    
print("\n------------ End Of fibbonacci series upto given number ---------------------")
    