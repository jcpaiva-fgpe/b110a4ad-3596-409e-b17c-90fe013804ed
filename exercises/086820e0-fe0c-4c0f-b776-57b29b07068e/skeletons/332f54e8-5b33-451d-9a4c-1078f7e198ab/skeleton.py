countries = set()
country = '?'

while (True):
    print('Country name?')
    country = input()
    
    if not country: break 
    if not country:
    	print(False)