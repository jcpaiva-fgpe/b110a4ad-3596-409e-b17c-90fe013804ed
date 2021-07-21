class Square: 
   a = 1.0
   def __init__(f, a):
        f.a = a
   def perimeter(f):
       return f.a * 4.0
k = Square(3)
print(k.perimeter())