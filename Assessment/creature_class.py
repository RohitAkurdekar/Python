# Internal asssessment

# parent class
EAT = "eat"
SLEEP = "sleep"
PLAY = "play"
WORK = "work"

class Creature:
    #class variable
    Category="MAMMAL"
    
    # class methods
    # returns catogory of object rxd
    @classmethod
    def get_category(myclass):
        return myclass.Category

    # set catogary of obj rxd
    @classmethod
    def set_catogary(myclass,rcv_catogary):
        myclass.Category = rcv_catogary

    # instance variables

    # declare and initialise variables
    def __init__(self,rcv_uniqueID:int,rcv_gender:str,rcv_current_activity:str) -> None:
        self.uniqueID = rcv_uniqueID
        self.gender = rcv_gender
        self.current_activity = rcv_current_activity

    # Instance methods
    # eat activity
    def eat(self):
        print("\nI am eating")
    
    # sleep activity
    def sleep(self):
        print("\nI am sleeping")

# child class
class Human(Creature):

    # declare and initialise variables
    def __init__(self,rcv_uniqueID:int,rcv_gender:str,rcv_current_activity:str,
                    rcv_Name:str,rcv_Age:int,rcv_City:str) -> None:
        super().__init__(rcv_uniqueID,rcv_gender,rcv_current_activity)
        self.Name = rcv_Name
        self.Age = rcv_Age
        self.City = rcv_City

    # instance methods
    def play():
        print("\nI am Playing")
    def work():
        print("\nI am Working")

    # display details
    def displayDet(self):
        print("\n----------- Human details are: -------------\n")
        print("Name: ",self.Name)
        print("Age : ",self.Age)
        print("City: ",self.City)
        print("Catogary: ",self.Category)
        
    # start activity
    def start_activity(self,rcv_activity):
        print("\nStarting activity ", rcv_activity)
        # Exception handling
        try:
            if rcv_activity == EAT:
                self.eat()
            elif rcv_activity == SLEEP:
                self.sleep()
            elif rcv_activity == PLAY:
                self.play()
            elif rcv_activity == WORK:
                self.work()
            else:
                # personal exception
                raise

        except:
            print("\nException: Jamnaar nahi.......")

