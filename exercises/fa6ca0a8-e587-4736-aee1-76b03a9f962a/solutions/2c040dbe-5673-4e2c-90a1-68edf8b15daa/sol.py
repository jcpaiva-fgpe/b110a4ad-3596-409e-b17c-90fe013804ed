
class Figure():
    def perimiter(s):
       return sum(s.sides)
    def __str__(s):
        return f'{s.__class__.__name__} {s.sides}'

class Square(Figure):
    def __init__(s, a):
        s.a = a
        s.sides = [s.a for i in range(4)]
    def area(s):
        return s.sides[0]**2

class Rectangle(Figure):
    def __init__(s, a, b):
        s.a = a
        s.b = b
        s.sides = [s.a, s.b, s.a, s.b]
    def area(s):
        return s.sides[0]*s.sides[1]

class RightTriangle(Figure):
    def __init__(s, a, b, c):
        s.a = a
        s.b = b
        s.c = c
        s.sides = [s.a, s.b, s.c]
    def area(s):
        return (s.sides[0]*s.sides[1])/2


l = [Square(7), Rectangle(5, 6),  RightTriangle(3, 4, 5)]
for i in l:
    print(i, i.perimiter(), i.area())