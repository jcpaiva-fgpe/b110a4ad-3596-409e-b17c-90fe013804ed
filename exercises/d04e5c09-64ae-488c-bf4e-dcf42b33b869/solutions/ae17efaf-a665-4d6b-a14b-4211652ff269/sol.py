def bli(li, b):
    if b < 1 or b > len(li): 
        return f"The second parameter: {b} is invalid."
    li.sort()
    
    def bli1(): 
        return li[-1]
    if b == 1: return bli1()
    li.remove(bli1())
    return(bli(li, b-1))

#############################################


""" <-- PUT A # ON THE BEGINNING of the line.
print(bli([3, 6, 8, 1, 4], 3))
#print(bli([2, 1, 8, 9, 4, 5], 2))
#print(bli([5], 1))
#""" 

try:
    li = list(map(int, input().split()))    # li - list, seqence of numbers (sep. by ',').
    b = int(input())                        # b - number.
    print(bli(li, b))                       # Call the function and display the result.
except ValueError:
    print("Wrong input data.")              #
# ----------------------------------------- #
