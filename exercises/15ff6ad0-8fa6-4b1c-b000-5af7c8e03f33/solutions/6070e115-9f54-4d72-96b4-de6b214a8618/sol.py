print('Podaj dwa rozne napisy dzielac je przecinkiem:')
zdania = input().split(",")

in1 = zdania[0].split() 
in2 = zdania[1].split()

print('Takie same wyrazy to:', *list(set(in1) & set(in2)))