tel = {'police': 997, 'fire brigade': 998, 'emergency': 999}
for k, v in tel.items():
    print(k + str(v).rjust(24 - len(k), '.'))