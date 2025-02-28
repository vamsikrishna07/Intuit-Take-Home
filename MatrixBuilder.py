import numpy as np
class MatrixBuilder:
    def build_matrix(self, cells):
        if not cells:
            return []
        x_max, y_max = -float('inf'), -float('inf')
        for x, y in cells:
            x_max = max(x, x_max)
            y_max = max(y, y_max)
        matrix = []
        for y in range(y_max+1):
            rows = []
            for x in range(x_max+1):
                rows.append('#' if (x,y) in cells else ' ')
            matrix.append(''.join(rows))
        return matrix