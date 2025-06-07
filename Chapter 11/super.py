class Employee :
    def __init__(self):
        print("Constructor of Employee")
    x  = 1

class Programmer (Employee) :
    def __init__(self):
        super().__init__()
        print("Constructor of Programmer")
    y = 2

class Manager (Programmer) :
    def __init__(self):
        super().__init__()
        print("Constructor of Manager")
    z = 3

# b = Employee()
# print(b.x)

# c = Programmer()
# print(c.x)
# print(c.y)

a = Manager()
print(a.x)
print(a.y)
print(a.z)