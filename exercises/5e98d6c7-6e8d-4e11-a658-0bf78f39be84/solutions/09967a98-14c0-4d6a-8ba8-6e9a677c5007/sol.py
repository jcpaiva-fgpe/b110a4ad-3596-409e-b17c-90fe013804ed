tel = {'gas emergency': 992, 'police': 997, 'fire brigade': 998, 'emergency': 999}

for k, v in tel.copy().items(): 
    if v % 3 == 0: 
       print(k)
       tel.pop(k)