def bli():
    pass


"""
print(bli([3,6,8,1,4], 3))
# """

#############################################
# TEST DATA ### DONT'T TOUCH THIS.          #
# ----------------------------------------- #
try:
    li = list(map(int, input().split(','))) # li - list, seqence of numbers (sep. by ',').
    b = int(input())                        # b - number.
    print(bli(li, b))                       # Call the function and display the result.
except ValueError:
    print("Wrong input data.")              #
# ----------------------------------------- #

