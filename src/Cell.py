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
            self.possibles = {1, 2, 3, 4, 5} \
                             - set([c.val for c in snapshot.cellsByRow(self.row)]) \
                             - set([c.val for c in snapshot.cellsByCol(self.col)])
        print(f'self.possibles={self.possibles}')
        return self.possibles

    def clone(self):
        return cell(self.row, self.col, self.val, self.possibles)
