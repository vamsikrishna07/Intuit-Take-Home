import numpy as np

class MatrixFolder:
    def fold(self, cells, fold):
        dir, value = fold
        new_cells = set()
        for x, y in cells:
            if dir == 'up':
                if y > value:
                    y = value - (y - value)
            elif dir == 'down':
                if y < value:
                    y = value + (value - y)
            elif dir == 'left':
                if x > value:
                    x = value - (x - value)
            elif dir == 'right':
                if x < value:
                    x = value + (x - value)
            else:
                continue
            new_cells.add((x,y))
        return new_cells
    
    def apply_folds(self, cells, folds):
        for fold in folds:
            cells = self.fold(cells, fold)
        return cells