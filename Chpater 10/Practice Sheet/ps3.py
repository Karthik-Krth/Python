a = 10

class Demo():
    a = 5

o = Demo() #class attribute
print(o.a)
o.a = 0  # instance attribute (Object)
print(o.a)