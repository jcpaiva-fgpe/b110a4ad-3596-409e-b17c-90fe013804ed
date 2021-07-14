w = {'energy emergency': 'pogotowie energetyczne', 'gas emergency': 'pogotowie gazowe', 'police': 'policja', 'fire brigade': u'straż pożarna', 'emergency': 'pogotowie ratunkowe'}

while True:
    print("Enter a word to translate:")
    word = input()
    if not word: break
    elif(word not in w.keys()): msg = "Unknown word!"
    else: msg = w[word]
    print(msg)
