w = {'energy emergency': 'pogotowie energetyczne', 'gas emergency': 'pogotowie gazowe', 'police': 'policja', 'fire brigade': u'straż pożarna', 'emergency': 'pogotowie ratunkowe'}

while True:
    print("Word?")
    word = input()
    if not word: break
    elif(word not in w.keys()): msg = "False!"
    else: msg = w[word]
    print(msg)
