# Import everything from creature class.py
from creature_class import *

#------------------- main() -------------------
def main():
    rohit = Human(1001,"Male",EAT,"ROHIT",26,"PUNE")
    rohit.displayDet()
    tempCatogary = input("\nEnter category of "+ str(rohit.Name) +" : ")
    rohit.set_catogary(tempCatogary)
    
    rohit.displayDet()

    rohit.start_activity(EAT)
    rohit.start_activity("DANCE")

    print("\n------------- End of Code ------------------")

main()