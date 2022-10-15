"""

-- try creating this 
Employee
  
  public emp_id
  private emp_salary
  protected mgr_id
  
  
  get_emp_salary()-> emp_salary
  set_emp_salary(rcv_salary)-> emp_salary
  
  

main


employee(100,1000,1)  

// direct access using .notation
empid
emp_salary
mgr_id


"""


class Employee:
    

    """ declaration of variable at class level which will get initialized 
        when constructor/object is created """

# public builtin function which get executed when object is created
    def __init__(self,rcv_emp_id,rcv_emp_salary,rcv_mgr_id)->None:
        self.emp_id = rcv_emp_id
        self._mgr_id = rcv_mgr_id
        self.__emp_salary = rcv_emp_salary

# return the salary of a particular employee object
    def get_emp_salary(self):
        return self.__emp_salary

# update the salary of a particular employee object
    def set_emp_salary(self,rcv_emp_salary):
        self.__emp_salary = rcv_emp_salary

def main():
    rohit = Employee(10,100,1)
    print(rohit.emp_id)
    
    #Exception handling
    try:
        print(rohit.__emp_salary)
    except: 
        print("unable to access private member")
    try:
        print(rohit._mgr_id)
    except: 
        print("unable to access protected member")

main()