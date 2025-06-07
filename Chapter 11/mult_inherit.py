class Employee:
    company = "Google"
    # nm = "Krth"
    def nam(self,nm):
        print(f"Name of the employee is {nm}")

class coder :
    lan = "Python"  
    def Show_lang(self):
        print(f"Your language  Name is {self.lan}")


class Programmer(Employee, coder):
    company = "Microsoft"
    def lang(self):
        print(f"Favorite language of programmer is {self.lan}")
    
              
a = Employee()
b = Programmer()
print(a.company,b.company)

b.Show_lang()
b.nam("Krth")
b.lang()

