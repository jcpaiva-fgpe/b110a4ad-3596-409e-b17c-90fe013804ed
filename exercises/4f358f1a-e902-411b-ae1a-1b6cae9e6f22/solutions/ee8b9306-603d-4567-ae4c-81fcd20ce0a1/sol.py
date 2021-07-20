def stars(num=15):
	return '*'*num


# ---------------------------------- #
# Test stars(). CAN'T TOUCH THIS.    #
# ---------------------------------- #
try: print(stars(int(input())))      #
except: print(stars())               #
# ---------------------------------- #