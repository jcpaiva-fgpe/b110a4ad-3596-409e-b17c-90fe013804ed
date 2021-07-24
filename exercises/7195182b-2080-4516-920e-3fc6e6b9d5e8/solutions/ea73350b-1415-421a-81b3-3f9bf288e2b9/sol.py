def knight(dimension, x = 0, y = 0):
    def jump (movement, x, y): # function trying to make another move
        nonlocal dx, dy, sz
        for k in range(8): # there are 8 possible knight moves
            xn = x + dx[k] # new coordinates
            yn = y + dy[k]
            if (xn in range(dimension)) and (yn in range(dimension)): # on the board?
               if sz[xn][yn] == 0:
                  sz[xn][yn] = movement # we save the current movement
                  if movement == dimension * dimension: return True # that was the last jump
                  if jump(movement + 1, xn, yn): return True # we try another one
                  sz[xn][yn] = 0 # failed attempta
        return False
    
    dx = ( 1,  2, 2, 1, -1, -2, -2, -1) # Possible movements (change x)
    dy = (-2, -1, 1, 2,  2,  1, -1, -2) # Possible movements (change y)
    sz = [ [0 for x in range(dimension)] for y in range(dimension) ] # chessboard
    sz[x][y] = 1 # starting point
    if not jump(2, x, y): 
        print("Failed.")
    else: 
        for y in range(dimension): # displaying the solution
            print('\n|', end='')
            for x in range(dimension):
                print(f"{sz[x][y]:2}", end="|")
                
d = int(input())
knight(d)