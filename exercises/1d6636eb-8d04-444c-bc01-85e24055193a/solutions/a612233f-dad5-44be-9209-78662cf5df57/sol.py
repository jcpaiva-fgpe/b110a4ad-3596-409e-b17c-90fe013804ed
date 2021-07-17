def root(x,y):
	return x**(1/y)

x = int(input('x:\n'))
y = int(input('y:\n'))

print(str(y) + '\u221A' + str(x), 'is:', root(x,y))