class Employee:
    company = "Google"
    def nam(self,nm):
        print(f"Name of the employee is {nm}")
    
# class Programmer:
#     company = "Microsoft"
#     def nam(self,nm):
#         print(f"Name of the Programmer is {nm}")
#     def lan(self,l):
#          print(f"Favorite language of programmer is {l}")


class Programmer(Employee):
    company = "Microsoft"
    def lan(self,l):
        print(f"Favorite language of programmer is {l}")
    
              
a = Employee()
b = Programmer()
print(a.company,b.company)