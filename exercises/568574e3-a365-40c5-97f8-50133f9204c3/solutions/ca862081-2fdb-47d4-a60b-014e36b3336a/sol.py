in1 = input('Podaj pierwszy napis: ').split()
in2 = input().split()
print('Takie same wyrazy to:', *list(set(in1) & set(in2)))
