def search_bin(list, searched):
    #Your code here
    pass


test = list(map(int, input().split()))
x = input("Val:\n")
r = search_bin(test, int(x))
print(f"Found in position {r}.") if r >= 0 else print("Not found.")