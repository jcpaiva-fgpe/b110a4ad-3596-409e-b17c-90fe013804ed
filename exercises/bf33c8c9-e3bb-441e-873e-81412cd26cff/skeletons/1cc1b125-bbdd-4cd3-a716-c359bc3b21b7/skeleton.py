dividend = int(input('dividend:')) 
for divisor in range (dividend-1,1, -1):
    if dividend % divisor == 0:
        print(dividend, 'print('In total', dividend, 'is divided without a remainder', amount, 'times.')', divisor)
        
print('In total', dividend, 'is divided without a remainder', amount, 'times.')