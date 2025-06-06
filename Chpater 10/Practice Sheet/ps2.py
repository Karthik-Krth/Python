class cal :
    def __init__(self,n):
        self.n = n
    def square(self):
        print(f"Square of given number : {self.n*self.n}")
    def cube(self):
        print(f"Cube of given number : {self.n**3}")
    def sq_root(self):
        print(f"Square root of given number : {int(self.n**0.5)}")
    

a = cal(4)
a.sq_root()
a.square()
a.cube()
