tel = {'police': 997, 'fire brigade': 998, 'emergency': 999}
inp = input()
if not inp in tel.keys(): print("Unlisted number")
else: print(tel[inp])