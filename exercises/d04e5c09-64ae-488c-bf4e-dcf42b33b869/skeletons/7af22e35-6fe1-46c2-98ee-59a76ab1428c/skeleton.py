# Example
def old_data(d):
    def month():
        return ['I','II','III','IV','V','VI','VII','VIII','IX','X','XI','XII'][int(d[1])-1]
    d = d.split('-')
    return d[2]+'.'+month()+'.'+d[0]

"""
print(old_data('2019-11-24'))
# """


#Your function
def bli():

    pass


"""
print(bli([3,6,8,1,4], 3))
# """

#############################################
# TEST DATA ### DON'T TOUCH THIS.           #
# ----------------------------------------- #
try:
    li = list(map(int, input().split(','))) # li - list, seqence of numbers (sep. by ',').
    b = int(input())                        # b - number.
    print(bli(li, b))                       # Call the function and display the result.
except ValueError:
    print("Wrong input data.")              #
# ----------------------------------------- #

