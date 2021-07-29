class Clothes:
    def __init__(u, material, color):
        u.material = material
        u.color = color
    def description(u):
        return u.material + ' in color: ' + u.color
class Jacket(Clothes):
    def description(u):
        return 'Jacket (' + Clothes.description(u) + ')'

"""
class Trousers(Clothes):
    def summer(u):
        return u.color == 'white'
"""
#u = Clothes('wool', 'gray')
k = Jacket('leather ', 'black') # ang. skora, czarny
#s = Trousers('jeans', 'blue')

print(k.description())
#print(k.leather())
#print(s.summer())



class Ubranie:\n\
    def __init__(u,material,kolor):\n\
        u.material = material\n\
        u.kolor = kolor\n\
    def opis(u):\n\
        return u.material+' w kolorze: '+u.kolor\n\
class Kurtka(Ubranie):\n\
    def opis(u):\n\
        return 'Kurtka ('+Ubranie.opis(u)+')'\n\
k=Kurtka(u'skóra','czarny')\n\
print k.opis()