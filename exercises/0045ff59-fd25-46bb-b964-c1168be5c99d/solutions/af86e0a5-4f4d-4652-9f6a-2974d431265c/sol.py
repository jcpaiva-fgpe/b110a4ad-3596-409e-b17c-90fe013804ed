tel = {'police': 997, 'fire brigade': 998, 'emergency': 999}
tel = dict(zip(tel.values(), tel.keys())) 
#tel = {v: k for k, v in tel.items()}
print(tel)