""" This is the file that we would intend to import from my_calculator.py"""

def my_add(a,b):
    print("my_add() from my_arithmatic_operation module was invoked")
    return a+b

def my_substract(a,b):
    print("my_substract() from my_arithmatic_operation module was invoked")
    return a+b    

""" This boiler plate code is used so that during import we indirectly dont run the my_add(1,2)
    code since python runs the entire file when imported """

if __name__ == "__main__":
    print("my_arithmatic_module is invoked directly with __name__:" , __name__ )
elif __name__ == "my_artihmatic_operation":
    print("my_arithmatic_module is invoked indirectly with __name__:" , __name__ )    
else:
    print("This will never be executed")    
