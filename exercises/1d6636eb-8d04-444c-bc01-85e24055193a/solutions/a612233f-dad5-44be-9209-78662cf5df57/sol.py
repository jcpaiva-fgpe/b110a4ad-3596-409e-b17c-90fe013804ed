def root(x, y):
	return x**(1/y)

x = int(input('x:\n'))
n = int(input('y:\n'))

print(str(n) + '\u221A' + str(x), 'is:', root(x,n))