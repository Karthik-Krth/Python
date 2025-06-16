class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Overloading the + operator
    def __add__(self, other):
        # Adding the coordinates of two Point objects
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"({self.x}, {self.y})"

# Create two Point objects
p1 = Point(2, 3)
p2 = Point(4, 5)

# Adding two Point objects using +
p3 = p1 + p2
print(p3)  # Output: (6, 8)
