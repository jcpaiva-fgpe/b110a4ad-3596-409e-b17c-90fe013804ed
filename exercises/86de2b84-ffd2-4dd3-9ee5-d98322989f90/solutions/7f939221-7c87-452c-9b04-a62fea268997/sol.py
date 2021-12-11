
def rk(a, b, c):

    delta = b**2 - 4*a*c
    if delta == 0:
        return -b/2*a

    elif delta > 0:
        x1 = (-b - delta**0.5)/2*a
        x2 = (-b + delta**0.5)/2*a
        return x1, x2
    else: return


# ------------------------------------ #
#     Do not change that code here     | 
# ------------------------------------ #
try:
    print(rk(*map(int, input().split())))  
except:
    #print(smash(1.2) #Example function #
    print(rk(-1,2,3))                  #
    print(rk(1,2,1))                   #
    print(rk(2,1,1))                   #
# ------------------------------------ #