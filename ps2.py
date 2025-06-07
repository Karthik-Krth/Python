class Animals :
    pass

class Pets (Animals):
    pass

class Dog (Pets):
    @staticmethod
    def bark():
        print("BOW BOW BOW !...")

a = Dog()

a.bark()