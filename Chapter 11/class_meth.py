class Demo:
    x = 1
    @classmethod
    def show(cls):
        print(f"the Class attribute value of X is {cls.x}")

o = Demo()
o.x = 33
o.show()
