#EXAMPLE FUNCTION old_date()
def old_date(d):
    def month():
        return ['I','II','III','IV','V','VI','VII','VIII','IX','X','XI','XII'][int(d[1])-1]
    d = d.split('-')
    return d[2]+'.'+month()+'.'+d[0]
#print(old_date('2019-11-24'))



#Your function
def bli():
    
    pass
#print(bli([3,6,8,1,4], 3))


#############################################
# TEST DATA ### DON'T TOUCH THIS.           #
# ----------------------------------------- #
print(bli(input().split(), int(input())))   #
#############################################

