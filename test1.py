print("Hello")

class Employee:
    def __init__(self,name,location,salary):
        self.emp_name = name
        self.emp_location = location
        self.emp_salary = salary

    def get_emp_info(self):
        print(f"""Employee Name :- {self.emp_name}
Employee Location :- {self.emp_location}
Employee Salary :- {self.emp_salary}""")

e = Employee("Ram","Pune",20000)
e.get_emp_info()


val1 = 255

val2 = 230

print("Area of Reactangle = ",val1 * val2)