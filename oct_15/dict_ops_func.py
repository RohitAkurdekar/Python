
# Accept dictionary elements


def accept_dict()->dict:
    my_dict = dict()

    max_len = int(input("Enter the maximum number of dict elements: "))
    for i in range(int(max_len)):
        my_keyWord = input("Enter a keyword: ")
        my_value = input("Enter a value: ")
        temp_data = {my_keyWord:my_value}
        my_dict.update(temp_data)
    return my_dict

# accept_dict()