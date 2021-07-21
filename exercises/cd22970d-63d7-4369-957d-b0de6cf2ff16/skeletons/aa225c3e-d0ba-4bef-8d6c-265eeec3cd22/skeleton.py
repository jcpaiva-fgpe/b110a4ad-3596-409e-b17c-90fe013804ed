class Clothes:
    def __init__(u, material, color):
        u.material = material
        u.color = color
    def description(u):
        return u.material + ' in color: ' + u.color
class Jacket(Clothes):
    def description(u):
        return 'Jacket (' + Clothes.description(u) + ')'

j = Jacket('lether', 'black')
print(j.description())