def search_bin(list, searched):
    left = 0
    right = len(list)
    while left <= right: 
        mid = (left + right) // 2
        middle = list[mid]
        if middle == searched: return mid
        if middle > searched: right = mid - 1
        else: left = mid + 1
    return -1

x = input("Enter the value: ")
r = search_bin(test, int(x))
print(f"Found in position {r}.") if r >= 0 else print("Not found.")