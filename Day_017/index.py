# create my own blueprint class

class Employee:
    # intiate our attrs , Self used to refer the object created
    # this a constructor that invoked when creating an object
    def __init__(self, name, age):
        self.name = name
        self.age  = age
        self.salary = 1500
    
    # create a general method
    def greet(self):
        print(f"Hey, {self.name} your age {self.age}")

    def net_salary(self, target):
        self.target = target
        return self.salary + (self.salary * self.target)
    
emp_1 = Employee("Ahmed", 25)
emp_1.greet()
print(emp_1.net_salary(0.30))
# to add an attr
# emp_1.address = "25st-port said"
# print(emp_1.address)