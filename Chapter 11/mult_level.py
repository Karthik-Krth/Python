class Employee :
    x  = 1

class Programmer (Employee) :
    y = 2

class Manager (Programmer) :
    z = 3

a = Manager()

print(a.x)
print(a.y)
print(a.z)
