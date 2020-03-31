# Template for the algorithm to solve a Futoshiki. Builds a recursive backtracking solution
# that branches on possible values that could be placed in the next empty cell. 
# Initial pruning of the recursion tree - 
#       we don't continue on any branch that has already produced an inconsistent solution
#       we stop and return a complete solution once one has been found

import pygame, Snapshot, Cell, Futoshiki_IO
from collections import Counter


def solve(snapshot, screen):
    # display current snapshot
    pygame.time.delay(300)
    Futoshiki_IO.displayPuzzle(snapshot, screen)
    pygame.display.flip()
    # if current snapshot is complete ... return a value
    if isComplete(snapshot):
        # print('return True *********************')
        return True

    next_empty_cell = snapshot.unsolvedCells()[0]

    for var in next_empty_cell.possibles:
        # print(f'var={var}')
        newsnapshot = snapshot.clone()
        newsnapshot.setCellVal(next_empty_cell.getRow(), next_empty_cell.getCol(), var)
        if checkConsistency(newsnapshot):
            if solve(newsnapshot, screen):
                return True

    return False


def checkConsistency(snapshot):
    for r in range(5):
        # print(k,v)
        for k, v in Counter([c.getVal() for c in snapshot.cellsByRow(r) if c.getVal() > 0]).items():
            if v >= 2:
                # print(f'check row Consistency={False}')
                return False
    for c in range(5):
        for k, v in Counter([c.getVal() for c in snapshot.cellsByCol(c) if c.getVal() > 0]).items():
            # print(k,v)

            if v >= 2:
                # print(f'check col Consistency={False}')
                return False
    # print(f'checkConsistency={True}')
    return True


def isComplete(snapshot):
    # print(f'len(snapshot.unsolvedCells())={len(snapshot.unsolvedCells())}')
    return len(snapshot.unsolvedCells()) == 0
