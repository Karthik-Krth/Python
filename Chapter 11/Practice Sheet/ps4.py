class Complex :
    def __init__(self,r,i):
        self.r = r
        self.i = i

    def __add__(self,other):
        return Complex(self.r + other. r ,self.i + other.i)
    
    def __mul__(self,ot):
        real =   self.r * ot.r - self.i *ot.i 
        img =    self.r * ot.i + self.i *ot.r
        return Complex(real , img)
    
    def __str__(self):
        return f"{self.r} + {self.i}i"

a = Complex(2,3)
b = Complex(5,6)
print(a+b)
print(a*b)