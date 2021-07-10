dividend = int(input('dividend:')) 
for divisor in range (dividend-1,1, -1):
    if dividend % divisor == 0:
        print(dividend, 'is divided without any remainder by', divisor)
        
print('In total', dividend, 'is divided without any remainder', amount, 'times.')