def root(x, y):
	return x**(1/y)

x = int(input())
n = int(input())

print(str(n) + '\u221A' + str(x), 'is:', root(x,n))