def power(x, n):
    return x**n
    
'''  
print(3, '^', 4, 'is:', power(3, 4))
print(4, '^', 3, 'is:', power(4, 3))
print(3, '^', 4, 'is:', power(x=3, n=4))
print(4, '^', 3, 'is:', power(n=3, x=4))
#'''


# Your root function
def root(x):
	return x**0.5

x = int(input())

print(str(2) + '\u221A' + x, 'is:', root(x))
# Expected output: n√x is: (here the result)