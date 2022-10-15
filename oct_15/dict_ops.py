"""	
2) Operations on Dictionary
     a) Please enter First Dictionary 
	 1) Please enter operation would you like to perform
		   1a) Merge Two dicts 
		           Take the second Dictionary from the user for this operation
		   2a) Check if the element is present in the dictionary 
		            Take the Input element that you would like to search
           3a) Append to the dictionary 
                   Take the Slice or individual element to add to the first dictionary		
"""

import dict_ops_func

my_func = dict_ops_func
def dict_ops():

    test = dict()
    my_dict = my_func.accept_dict()
    
    while True:
        my_func.dict_menu()
        dict_choice = 0
        dict_choice = int(input("Enter your choice: "))
    
        if dict_choice == 1:    # add another dict
            add_dict = my_func.accept_dict()
            my_func.add_dict(my_dict,add_dict)

        elif dict_choice == 2: # element present or not?
            try:                            # get the index of element
                print("Element found at ",my_dict.index(int(input("Enter a element to be searched: "))+1))
            except ValueError:
                print("Element not present in dict")
        
        elif dict_choice == 3: # Append to the dict 
            try:
                my_dict.append(int(input("Enter element to be inserted: ")))
                print(my_dict)
            except:
                print("element can not be empty")
        elif dict_choice == 4:
            break

    print("\n----------------------------------")

dict_ops()