while True:
    word = input()
    if not word: break
    elif(word not in w.keys()): msg = "Unknown word"
    else: msg = w[word]
    print(msg)