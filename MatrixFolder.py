import numpy as np

class MatrixFolder:
    def fold(self, cells, fold):
        dir, value = fold
        cells = cells.copy()
        if dir == 'up' or dir == 'down':
            if dir == 'up':
                mask = cells[:,1] > value
                cells[mask, 1] = value - (cells[mask, 1] - value)
            else:
                mask = cells[:,1] < value
                cells[mask, 1] = value + (value - cells[mask, 1])
        elif dir == 'left' or dir == 'right':
            if dir == 'left':
                mask = cells[:,0] > value
                cells[mask, 0] = value - (cells[mask, 0] - value)
            else:
                mask = cells[:,0] < value
                cells[mask, 0] = value + (value - cells[mask, 0])
        cells = np.unique(cells, axis=0)
        return cells
    
    def apply_folds(self, cells, folds):
        for fold in folds:
            cells = self.fold(cells, fold)
        return cells