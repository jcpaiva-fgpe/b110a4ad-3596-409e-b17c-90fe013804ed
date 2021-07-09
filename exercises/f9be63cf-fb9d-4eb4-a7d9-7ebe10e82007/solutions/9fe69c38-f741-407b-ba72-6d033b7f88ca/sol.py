print('Number of employment contracts:') 
employment_contracts = int(input()) # Integers only
    
print('Commuter? True or False?')
commuter = input()

costs = 0 # overwrite 
if employment_contracts == 1: 
    costs = 3600 if commuter == "True" else 3000
elif employment_contracts > 1: 
    costs = 5400 if commuter == "True" else 4500
else: costs = costs

print('The annual costs of revenue is', costs, u'zł.')