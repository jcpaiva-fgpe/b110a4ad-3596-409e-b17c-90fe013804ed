countries = set()
country = '?'

while (True):
    print('Country name?')
    country = input()
    
    if not country: break # Test issue.
    if country in countries:
    	print(False)
        
    else: countries.add(country)