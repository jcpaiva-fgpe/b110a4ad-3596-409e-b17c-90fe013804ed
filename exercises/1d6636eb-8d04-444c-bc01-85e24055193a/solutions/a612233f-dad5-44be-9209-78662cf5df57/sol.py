def root(x, y):
	return x**(1/y)

x = int(input('x:\n'))
n = int(input('n:\n'))

print(str(n) + '\u221A' + str(x), 'is:', root(x,n))