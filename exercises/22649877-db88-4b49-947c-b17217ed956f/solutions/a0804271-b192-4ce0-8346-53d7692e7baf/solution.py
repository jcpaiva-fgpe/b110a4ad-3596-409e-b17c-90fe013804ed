napis = input().lower().split()
d = {napis[i]: j.count('a') for i, j in enumerate(napis)} 
try:
    print(max(d, key = d.get))
except ValueError:
    print()