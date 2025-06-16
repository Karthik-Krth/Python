class Book:
    def __init__(self, pages):
        self.pages = pages

    def __add__(self,x):
        # Adding pages of two books
        return self.pages + x.pages

b1 = Book(100)
b2 = Book(150)

# Adding two Book objects
print(b1 + b2)  # Output: 250
