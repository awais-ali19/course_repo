# Write a Python class Employee with attributes like emp_id, emp_name, emp_salary, 
# and emp_department and methods like calculate_emp_salary, emp_assign_department, and print_employee_details.
# Sample Employee Data:
# "ADAMS", "E7876", 50000, "ACCOUNTING"
# "JONES", "E7499", 45000, "RESEARCH"
# "MARTIN", "E7900", 50000, "SALES"
# "SMITH", "E7698", 55000, "OPERATIONS"

# Use 'assign_department' method to change the department of an employee.
# Use 'print_employee_details' method to print the details of an employee.
# Use 'calculate_emp_salary' method takes two arguments: salary and hours_worked, 
# which is the number of hours worked by the employee. If the number of hours worked is more than 50,
# the method computes overtime and adds it to the salary. Overtime is calculated as following formula:
# overtime = hours_worked - 50
# Overtime amount = (overtime * (salary / 50))

class Employee:
    def __init__(self , emp_name , emp_id , emp_salary , emp_department):
        self.emp_id=emp_id
        self.emp_name=emp_name
        self.emp_salary=emp_salary
        self.emp_depart=emp_department
    def calculate_emp_salary(self,salary,hours_worked):
        if hours_worked > 50:
            overtime = hours_worked - 50
            Overtime_amount = (overtime * (salary / 50))
            self.emp_salary=Overtime_amount + salary
    def emp_assign_department(self,dept):
        self.emp_depart=dept
    def print_employee_details(self):
        print(f"Name:  {self.emp_name}")  
        print(f"ID:  {self.emp_id}")
        print(f"Salary:  {self.emp_salary}")
        print(f"Department:  {self.emp_depart}") 
        print("--------------------------")
        
e1=Employee("ADAMS", "E7876", 50000, "ACCOUNTING")
e2=Employee("JONES", "E7499", 45000, "RESEARCH")
e3=Employee("MARTIN", "E7900", 50000, "SALES")
e4=Employee("SMITH", "E7698", 55000, "OPERATIONS")

print("Original Employee Details")
e1.print_employee_details()
e2.print_employee_details()
e3.print_employee_details()
e4.print_employee_details()

#change the department of employee 1 and 3
e1.emp_assign_department("Sales")
e3.emp_assign_department("ACCOUNTING")

#calculate the salary of overtime
e2.calculate_emp_salary(45000,52)

print("Update Employee Details") 
e1.print_employee_details()
e2.print_employee_details()
e3.print_employee_details()
e4.print_employee_details()
       




       