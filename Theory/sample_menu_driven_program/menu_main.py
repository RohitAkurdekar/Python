""" This is our main program where we print the menu """
import utilities

#--- MENU ENDS
while(True):
    print("\n-----------------------------------------------------------------------------------")
    print("DIOT STORE")
    print("-----------------------------------------------------------------------------------")
    print("Welcome User , What would you like to do today?")
    print("-----------------------------------------------------------------------------------")
    print("1) Operations on List")
    print("2) Operations on Dictionary")
    print("3) Operations on Set")
    print("4) Operations on strings ")
    print("5) Exit")
    
    choice = int(input("Please enter you choice"))
    
    if choice ==1:
        utilities.func_choice1() 
    elif choice ==2:
        utilities.func_choice2() 
    elif choice ==3:
        utilities.func_choice3()  
    elif choice ==4:
        utilities.func_choice4()  
    elif choice ==5:
        print("Thank you for using DIOT store today!!! Visit again")
        break
    else:
        print("Please enter correct choice !!!")
#--- MENU ENDS  