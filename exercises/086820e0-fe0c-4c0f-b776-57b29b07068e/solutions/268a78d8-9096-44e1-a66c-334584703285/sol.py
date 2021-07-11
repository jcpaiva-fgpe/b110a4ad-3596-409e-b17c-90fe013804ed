countries = set()
country = '?'

while (True):
    #print('Please name a country:')
    country = input()
    
    if not country: break # Test issue.
    if country in countries:
    	print('The name was mentioned before!')
        
    else: countries.add(country)