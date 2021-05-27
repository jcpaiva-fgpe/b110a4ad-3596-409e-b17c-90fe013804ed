napis = input().lower().split()
d = {napis[i]: j.count('a') for i, j in enumerate(napis)} 
print(f'{max(d, key = d.get)}')
