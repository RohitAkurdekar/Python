"""Utilities function here """  

#---------------------------
def add_two_lists(input_list1):
        #Take the second list from the user for this operation
        input_list2 = list(input("Please enter the values for the second list"))

        is_number_list = input("Are the number lists: Type Y/N").upper

        list1_len = len(input_list1)
        list2_len = len(input_list2)
        
        if list1_len == 0 or list1_len== 0:
            raise ValueError("One of the list is empty")

        new_list=[]
        for i in range(0,max(list1_len,list2_len)):
            if is_number_list=='Y':
                if input_list1[i] < 0 or input_list2[i]<0:
                    raise ValueError("List cannot contain negative numbers")
                
                new_list.append( int(input_list1[i])+int(input_list1[i]))
            else:
                new_list.append( input_list1[i]+input_list1[i])

        print("After addition the new list is " , new_list)

"""Note : raise an exception if the users inserts a negative number in case he chooses to input
    a list of numbers OR he inputs empty list """


def element_exists(input_list,element_to_search):
    try:
        print("Number found on index " ,  input_list.index(element_to_search))
    except ValueError:
        raise ValueError(element_to_search," is not present in the list ")
        #Note : raise an exception if the element is not found in the list

def append_element(input_list1):
        #Take the Slice or individual element to add to the first list	
        to_append_element = input("individual element to add to the first list")
        input_list1.append(to_append_element)
        print(to_append_element, " has been added successfully, Here is the new list : " , input_list1 )

"""sample method to merge two dictionary 
first_dict = {"India":"Delhi"}
second_dict = {"US":"DC"}
"""

def merge_dict(first_dict,second_dict):
    first_dict_copy = first_dict.copy()
    first_dict_copy.update(second_dict)
    print(first_dict_copy)

#merge_dict(first_dict,second_dict)

def func_choice1():
    input_list1 = list(input("Please enter the values for the first list"))
    #- submenu for the list
    print("1 Add Two lists in order of their insert")
    print("2 Check if the element is present in the list")
    print("3 Append to the list ")
    sub_operation = int(input("Please enter operation would you like to perform"))
    
    if sub_operation ==1:
          add_two_lists(input_list1)              
    elif sub_operation ==2:
        element_to_search = input("Please Input element that you would like to search")
        element_exists(input_list1,element_to_search)
    elif sub_operation ==3:
        append_element(input_list1)

    return True

def func_choice2():
    print("Feature will be Added soon , Sorry for inconvinence caused !!!") 

def func_choice3():
    print("Feature will be Added soon , Sorry for inconvinence caused !!!") 

def func_choice4():
    print("Feature will be Added soon , Sorry for inconvinence caused !!!")  


"""
     a) Please enter First Dictionary 
	 1) Please enter operation would you like to perform
		   1a) Merge Two lists 
		           Take the second Dictionary from the user for this operation
		   2a) Check if the element is present in the list 
		            Take the Input element that you would like to search
           3a) Append to the dictionary 
                   Take the Slice or individual element to add to the first dictionary		   

     a) Please enter First set 
	 1) Please enter operation would you like to perform
		   1a) Check if the element is present in the list 
		            Take the Input element that you would like to search
           3a) Add to the set 
                   Add aN Individual element to add to the first set

      Please enter the string
	  1) Display upper case of the string
	  2) Concatenate "Hello" literal to the existing string received
	  3) Output true if the string has letter 'a' in it 

"""