class Person:
    def __init__(self, nm):
        self.nm = nm

    @property
    def name(self):
        return self.nm

    @name.setter
    def name(self, value):
        if len(value) < 3:
            print("Name is too short!")
        else:
            self.nm = value

p = Person("Alice")
print(p.name)  # Alice

p.name = "Al"   # Too short, won't set
p.name = "Bob"  # Valid, will set
print(p.name)   # Bob
