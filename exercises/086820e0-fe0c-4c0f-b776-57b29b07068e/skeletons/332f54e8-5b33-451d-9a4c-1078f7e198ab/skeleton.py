countries = set()
country = '?'

while (True):
    print('Name the country:')
    country = input()
    
    if not country: break 
    if not country:
    	print('The name was mentioned before!')