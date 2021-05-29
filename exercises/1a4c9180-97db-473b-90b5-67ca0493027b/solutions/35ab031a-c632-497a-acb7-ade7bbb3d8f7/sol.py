litera = 'A'
while True:
    print(f"Podaj slowo na litere {litera}:")
    slowo = input().upper()
    if slowo[0] == litera:
        litera = slowo[-1]
    else:
        print("Przegrales.")
        break
