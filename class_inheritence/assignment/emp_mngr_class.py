"""
# use inheritance to solve this problem
Employee (
-- class variables and methods
organisation_name, get_organisation_name(),set_organisation_name(org_name)

-- instance variables and methods()
,emp_id,name,base_location,deployed_location,designation,salary ,get_employee_details() 	


-- subclass of Employee
Manager(
	-- instance variables and methods()
	managed_employees[],
	perform_appraisal_for_an_employee(emp_id,percent_raise),
	get_manager_details(mgr_id)
)
		
"""
#defines
MANAGER = "MANAGER"
EMPLOYEE = "EMPLOYEE"

# Parent class
class Employee:
    # class variable
    organisation_name = "A&IOEans"

    # initialisation
    def __init__(self,rcv_emp_id,rcv_name,rcv_base_location,rcv_deployed_location,
    rcv_designation,rcv_salary) -> None:
        self.emp_id = rcv_emp_id
        self.name = rcv_name
        self.base_location = rcv_base_location
        self.deployed_location = rcv_deployed_location
        self.designation = rcv_designation
        self.salary = rcv_salary
    
    # Display details of employee
    def get_employee_details(self)->None:
        print("\n-------- Emp details: ----------------------\n")
        print("Emp_id: ",self.emp_id)
        print("Name: ",self.name)
        print("Base location: ",self.base_location)
        print("Deployed location: ",self.deployed_location)
        print("Designation: ",self.designation)
        print("Salary: ",self.salary)

    # set organisation name
    @classmethod
    def set_organisation(myclass,rcv_organisation)->None:
        myclass.organisation_name = rcv_organisation
    
    # get organisation name
    def get_organisation(myclass)->str:
        return myclass.organisation_name
# ------------------ End of Employee class --------------------------------    

#child class
class Manager(Employee):

    def __init__(self,rcv_emp_id,rcv_name,rcv_base_location,rcv_deployed_location,
    rcv_designation,rcv_salary,rcv_managed_employees):

        super().__init__(rcv_emp_id,rcv_name,rcv_base_location,
        rcv_deployed_location,    rcv_designation,rcv_salary)
        
        # employee list
        self.managed_employees = rcv_managed_employees

# appraisal
    def perform_appraisal_for_an_employee(self,rcv_emp_id,rcv_percent_raise):
        emp_found = False
        for emp in self.managed_employees:
            if emp.emp_id == rcv_emp_id:
                emp.salary = emp.salary + emp.salary*rcv_percent_raise/100
                emp_found = True

        if not emp_found:
            print("Employee details not found in manager's emp list")
        
    
    # get manager's details
    def get_manager_details(self):
        self.get_employee_details()

    # get employees under manager
    def get_employees_under_manager(self):
        print("---------------------------")
        print("\nEmployees under ",self.name," are:")
        for emp in self.managed_employees:
            print(emp.name)
