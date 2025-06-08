class Vector:
    def __init__(self,i,j,k):
        self.i = i
        self.j = j
        self.k = k

    def __add__(self,other):
        return Vector(self.i + other.i ,self.j + other.j , self.k + other.k)
    
    def __mul__(self,other):
        return (self.i * other.i + self.j * other.j + self.k * other.k)
    
    def __str__(self):
        return f" Vector {self.i} , {self.j} , {self.k} "



a = Vector(2,3,4)
b = Vector(5,6,7)
print(a+b)
print(a*b)