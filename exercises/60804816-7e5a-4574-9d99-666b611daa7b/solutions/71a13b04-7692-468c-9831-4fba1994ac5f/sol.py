class Rectangle:
    a = b = 1.0
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return f'Rectangle ({self.a}, {self.b})'
    def perimeter(self):
        return 2*self.a + 2*self.b
    def area(self):
        return self.a*self.b


p = Rectangle(3, 4)
print(p)
print(p.perimeter())
print(p.area())