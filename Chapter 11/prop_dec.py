class Employee :
    name = "Krth"
    def Show(self):
        print(f"Name of the employee {self.name}")

    @property
    def Age(self):
        return self.vayasu
    
    @Age.setter
    def Age(self,value):
        self.vayasu = value 
    
o = Employee()

o.Age = 23

print(f"Age of {o.name} is  {o.vayasu}")