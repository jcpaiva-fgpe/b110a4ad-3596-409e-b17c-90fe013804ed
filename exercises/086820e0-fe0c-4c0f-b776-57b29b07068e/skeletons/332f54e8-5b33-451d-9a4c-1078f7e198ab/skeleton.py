countries = set()
country = '?'

while (True):
    #print('Please name a country:')
    country = input()
    
    if not country: break 
    if not country:
    	print('The name was mentioned before!')