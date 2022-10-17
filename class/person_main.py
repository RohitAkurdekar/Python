from person_class import Person

def main():
# Rohit is an Object of a class person
    Rohit = Person("Rohit","Male","Engineer")
    Rohit.setStudyBehaviour()
    Rohit.setWorkBehaviour("Never studies")     # multiple ways to pass data

    Rohit.displayDet()       # calling func to display details


# Saurav is an Object of a class person
    Saurav = Person("Saurav","Male","Engineer")
    Saurav.setStudyBehaviour()      # setting study behaviour
         # multiple ways to pass data
    Saurav.setWorkBehaviour(input("Enter work behaviour: ")) 

    Saurav.displayDet()       # calling func to display details

main()