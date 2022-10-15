"""
1) Operations on List
     a) Please enter First list 
	    Note : raise an exception if the users inserts a negative number 
            in case he chooses to input a list of numbers OR he inputs empty list 
	 1) Please enter operation would you like to perform
		   1a) Add Two lists in order of their insert 
		           Take the second list from the user for this operation
		   2a) Check if the element is present in the list 
		            Take the Input element that you would like to search
					Note : raise an exception if the element is not found in the list
           3a) Append to the list 
                   Take the Slice or individual element to add to the first list	
"""

import list_ops_func

my_func = list_ops_func
def list_ops():

    my_list = my_func.accept_list()
    while True:
        list_ops_func.list_menu()
        list_choice = 0
        list_choice = int(input("Enter your choice: "))
    
        if list_choice == 1:    # add another list
            add_list = my_func.accept_list()
            my_func.add_list(my_list,add_list)

        elif list_choice == 2: # element present or not?
            try:                            # get the index of element
                print("Element found at ",my_list.index(int(input("Enter a element to be searched: "))+1))
            except ValueError:
                print("Element not present in list")
        
        elif list_choice == 3: # Append to the list 
            try:
                my_list.append(int(input("Enter element to be inserted: ")))
                print(my_list)
            except:
                print("element can not be empty")
        elif list_choice == 4:
            break

    print("\n----------------------------------")



    

# list_ops()