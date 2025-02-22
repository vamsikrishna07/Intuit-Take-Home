import numpy as np
class MatrixBuilder:
    def build_matrix(self, cells):
        if cells.size == 0:
            return []
        x_max = int(np.max(cells[:,0]))
        y_max = int(np.max(cells[:,1]))
        s = { (int(x), int(y)) for x,y in cells }
        matrix = []
        for y in range(y_max+1):
            rows = []
            for x in range(x_max+1):
                rows.append('$' if (x,y) in s else ' ')
            matrix.append(''.join(rows))
        return matrix