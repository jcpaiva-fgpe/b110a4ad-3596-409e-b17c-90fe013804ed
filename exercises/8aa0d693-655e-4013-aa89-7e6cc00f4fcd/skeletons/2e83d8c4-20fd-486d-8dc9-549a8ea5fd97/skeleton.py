class Clothes:
    def __init__(u, material, color):
        u.material = material
        u.color = color
    def description(u):
        return u.material + ' in color: ' + u.color
class Jacket(Clothes):
    def leather(u):
        return u.material == 'leather'
class Trousers(Clothes):
    def summer(u):
        return u.color == 'white'

u = Clothes('wool', 'gray')
k = Jacket('leather', 'black')
s = Trousers('jeans', 'blue')

print(u.description())
print(k.leather())
print(s.summer())