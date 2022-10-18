# include class files
from emp_mngr_class import EMPLOYEE,Employee,MANAGER,Manager

def main():
    # object of parent class: Employee
    employee1 = Employee(1001,"Python","Kolhapur","Mumbai",EMPLOYEE,5000)
    employee2 = Employee(1002,"Django","Delhi","Mumbai",EMPLOYEE,8000)
    employee3 = Employee(1003,"Flask","Patna","Delhi",EMPLOYEE,7000)

    # object of parent class: Employee
    employee4 = Employee(1004,"Java","Kolhapur","Chennai",EMPLOYEE,9000)
    employee5 = Employee(1005,"Html","Kerala","Mumbai",EMPLOYEE,10000)
    employee6 = Employee(1006,"Cpp","Nagpur","Delhi",EMPLOYEE,6000)

    tempList = [employee1,employee2,employee3]
    # object of child class: Manager
    manager1 = Manager(2001,"Rohit","Pune","Mumbai",MANAGER,50000,tempList)

    tempList = [employee4,employee5,employee6]
    # object of child class: Manager
    manager2 = Manager(2002,"Amit","Mumbai","Pune",MANAGER,45000,tempList)

    employee1.get_employee_details()
    
    manager1.get_manager_details()
    
    manager2.get_manager_details()
    print("---------------\nbefore appraisal")
    employee2.get_employee_details()

    manager1.perform_appraisal_for_an_employee(1002,10)

    print("---------------\n After appraisal ")
    employee2.get_employee_details()

    # get employees under particular manager
    manager1.get_employees_under_manager()
    manager2.get_employees_under_manager()

    print("\n------------ EoC -----------------------------\n")

main()