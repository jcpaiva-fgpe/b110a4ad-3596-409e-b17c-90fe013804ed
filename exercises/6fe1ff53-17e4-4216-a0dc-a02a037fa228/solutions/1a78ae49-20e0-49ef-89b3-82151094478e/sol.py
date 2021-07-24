class Queens:
    def __init__(self, dimension):
        self.dimension = dimension # chessboard dimension (number of columns)
        self.a = {i: True for i in range(1, dimension + 1)}
        # a[i] a[i] means no queen in the i-th line
        self.b={i: True for i in range(2, 2 * dimension + 1)}
        # b[i] means no queen in the i-th diagonal /
        self.c={i: True for i in range(1 - dimension, dimension)}
        # c[i] means no queen in the i-th diagonal \
        self.x={ }
        # x[i] contains a fixed position of the queen in the i-th column
    
    def set(self, i = 1): # i - column number
        for j in range(1, self.dimension + 1): # j - line number
            if self.a[j] and self.b[i + j] and self.c[i - j]:
                self.x[i] = j # we try to put on [i, j]
                self.a[j] = self.b[i + j] = self.c[i - j] = False # we mark that occupied
                if i == self.dimension: return True # it was the last queen
                if not self.set(i + 1): # failed to put in another queen
                    self.a[j] = self.b[i + j] = self.c[i - j] = True # we mark free
                else: return True 
        return False # failed to put in this queen

    def __str__(self):
        rx = dict(zip(self.x.values(), self.x.keys()))
        s = ""
        for j in range(1, self.dimension + 1):
            s += '|' + '+|' * (rx[j] - 1) + 'H|' + '+|' * (self.dimension - rx[j]) + '\n'
        return s
    
checkerboard = Queens(8)
checkerboard.set()
print(str(checkerboard)[:-1])