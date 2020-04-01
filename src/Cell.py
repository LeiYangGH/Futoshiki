# This is a cell in a Futoshiki, consisting of x, y coordinates (column and row) and a value. 
# All parameters are integers between 1..5, values can also be 0 indicating that the value is still unknown.

class cell:
    def __init__(self, row, col, val):
        self.row = row
        self.col = col
        self.val = val
        self.possibles = {}

    def getRow(self):
        return self.row

    def setRow(self, row):
        self.row = row

    def getCol(self):
        return self.col

    def setCol(self, col):
        self.col = col

    def getVal(self):
        return self.val

    def setVal(self, val):
        self.val = val

    def getPossibles(self, snapshot):
        if not self.possibles:
            fullset = {1, 2, 3, 4, 5}
            for (coords1, coords2) in snapshot.getConstraints():
                if coords1[0] == self.row and coords1[1] == self.col: #self is smaller
                    var_big = snapshot.getCellVal(coords2[0], coords2[1])
                    print(f'var_big={var_big}')
                    if var_big == 0:
                        var_big = 5
                        print(f'fix var_small={var_big}')
                    for big in range(var_big,6):
                        if big in fullset:
                            fullset.remove(big)
                            print(f'remove big {big}')
                if coords2[0] == self.row and coords2[1] == self.col: #self is bigger
                    var_small = snapshot.getCellVal(coords1[0], coords1[1])
                    print(f'var_small={var_small}')
                    if var_small == 0:
                        var_small = 1
                        print(f'fix var_small={var_small}')
                    for small in range(1, var_small+1):
                        if small in fullset:
                            fullset.remove(small)
                            print(f'remove small {small}')



                # var1 = snapshot.getCellVal(coords1[0], coords1[1])
                # var2 = snapshot.getCellVal(coords2[0], coords2[1])
            self.possibles = fullset \
                             - set([c.val for c in snapshot.cellsByRow(self.row)]) \
                             - set([c.val for c in snapshot.cellsByCol(self.col)])
        print(f'self.possibles={self.possibles}')
        return self.possibles

    def clone(self):
        return cell(self.row, self.col, self.val, self.possibles)
