def avg(*arg):
    s = 0
    if len(arg) != 0:
        for x in arg:
            s += x
        return s/len(arg)
    
    return "Call the function with at least one arg."

print(avg(*range(1, 100, 2)))