# functions of list operation 

# display menu of list
def list_menu():
    print("\n----------------------------------")
    print("1.Add Two lists")
    print("2.Check if the element is present in the list")
    print("3.Append to the list")
    print("4.Exit")

# accept 2nd list and return 
def accept_list()->list:
    print("\n----------------------------------")

    list_len = int(input("Enter maximum number of elements: "))
    my_list = list()
    i=0
    while(i<list_len):
        try:
            my_list.append(int(input("Enter element of list: ")))
            i+=1
        except:
            print("Value can not be empty......!!!")
    return my_list

# add lists
def add_list(list1:list,list2:list):
    result_list=list()
    if(len(list1)!= len(list2)):
        print("list lengths are not same.......!!!")
    else:
        for i in range(len(list1)+1):
            try:
                result_list.append(int(list1[i])+int(list2[i]))
            except IndexError:
                print("Array index out of range")
        print("after addition:")
        print(result_list)
