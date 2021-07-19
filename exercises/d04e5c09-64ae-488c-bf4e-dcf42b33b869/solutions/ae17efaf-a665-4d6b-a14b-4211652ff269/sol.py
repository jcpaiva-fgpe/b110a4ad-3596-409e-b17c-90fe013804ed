def bli(li, b):
    if b < 1 or b > len(li): 
        return f"The second parameter: {b} is invalid."
    li.sort()
    
    def bli1(): 
        return li[-1]
    if b == 1: return bli1()
    li.remove(bli1())
    return(bli(li, b-1))

try:
    li = list(map(int, input().split(','))) # Expecting a seqence of numbers (sep. by ',')
    b = int(input())
    print(bli(li, b)) # Call the function and display the result

except ValueError:
    print("Wrong input data.")


"""
print(bli([3,6,8,1,4], 3))
# """