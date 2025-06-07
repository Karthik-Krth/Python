class Employee  :
    def __init__(self,sal,inc):
        self.sal = sal
        self.inc = inc
        
    def salary (self):
        print(f"Salary of the employee is {self.sal}")

    def increment (self):
        print(f"The salary is incremented ... to {self.inc}")

    @property
    def SalaryAfterIncrement(self):
        return self.sal+self.inc
    
    @SalaryAfterIncrement.setter
    def SalaryAfterIncrement(self,value):
        self.inc = value - self.sal

o = Employee(20000,1000)
o.salary()
o.increment()
print(f"salary After increment is {o.SalaryAfterIncrement}")
o.SalaryAfterIncrement = 25000
print(f"Increment is {o.inc}")
