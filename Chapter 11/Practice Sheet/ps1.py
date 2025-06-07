class Two_D :
    # x = 9
    # y = 6
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def show(self):
        print(f" The 2D vector is {self.x}i + {self.y}j")

class Three_D (Two_D):
    # z = 3
    def __init__(self,x,y,z):
        super().__init__(x,y)
        self.z = z
    def show(self):
        print(f" The 3D vector is {self.x}i + {self.y}j + {self.z}k")
        
a = Two_D(1,2)
a.show()
b = Three_D(3,4,5)
b.show()

