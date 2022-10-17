# class example
class Person:
    # private variables
    __workBehave = ""
    __studyBehave = ""
    # init variables
    def __init__(self,rcv_name,rcv_Sex,rcv_Profession)->None:
        #public variables, Init at obj creation
        self.Name = rcv_name
        self.Sex = rcv_Sex
        self.Profession = rcv_Profession
        
    # set Name
    def setName(self,rcv_name)->None:
        self.Name = rcv_name
    
    # set Sex
    def setSex(self,rcv_Sex)->None:
        self.Sex = rcv_Sex
    
    # set profession
    def setProfession(self,rcv_Profession)->None:
        self.Profession = rcv_Profession
    
    # set working behaviour
    def setWorkBehaviour(self,rcv_workBehave)->None:
        self.__workBehave = rcv_workBehave
    
    # set study behaviour
    def setStudyBehaviour(self)->None:
        self.__studyBehave = input("Enter study behaviour: ")

    # get working behaviour
    def getWorkBehaviour(self)->str:
        return self.__workBehave
    
    # get study behaviour
    def getStudyBehaviour(self)->str:
        return self.__studyBehave

    #display all details
    def displayDet(self)->None:
        print("------------------------------------------------")
        print("Name: ",self.Name)
        print("Sex: ",self.Sex)
        print("Profession: ",self.Profession)
        print("Study():",self.getStudyBehaviour())
        print("Work():",self.getWorkBehaviour())
        print("------------------------------------------------")
    
