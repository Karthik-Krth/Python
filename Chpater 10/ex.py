class Dog:
    def sound(self):
        print("Bark!")

class Cat:
    def sound(self):
        print("Meow!")

def make_sound(animal):
    animal.sound()

make_sound(Dog())  # Bark!
make_sound(Cat())  # Meow!
