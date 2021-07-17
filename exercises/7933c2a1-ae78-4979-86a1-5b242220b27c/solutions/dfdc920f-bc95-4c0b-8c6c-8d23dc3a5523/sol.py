def avg(*arg):
    s = 0
    if len(arg) != 0:
        for x in arg:
            s += x
        return s/len(arg)
    return s

### Do not change that code here ##### 
print(avg(*map(int, input().split())))  
######################################

""" <-- Example: PUT A # ON THE BEGINNING of the line.

x, y = map(int, input().split())

x = input()
y = input()

print(avg())         # Withouut arg 
print(avg(x))        # one arg
print(avg(x,y))      # two args

#""" 
####### EOF - End of file. ##########
#####################################
