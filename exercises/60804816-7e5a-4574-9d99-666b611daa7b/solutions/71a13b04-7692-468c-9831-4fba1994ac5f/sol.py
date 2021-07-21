class Rectangle:
    a = b = 1.0
    def __init___(f, a, b):
        f.a = a
        f.b = b
    def __str__(f) -> str:
        return f'{f.a}{f.b}'
    def perimeter(f):
        return 2*f.a + 2*f.b
    def area(f):
        return f.a*f.b