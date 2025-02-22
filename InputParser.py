import numpy as np
class InputParser:
    def __init__(self, file_path):
        self.file_path = file_path
    
    def parse(self):
        cells, folds = set(), []
        with open(self.file_path) as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                if line[:4] == "cell":
                    coordinates = line.split()[-1]
                    x_coord, y_coord = coordinates.split(',')
                    x = int(x_coord.split("=")[-1])
                    y = int(y_coord.split("=")[-1])
                    cells.add((x,y))
                elif line[:4] == "fold":
                    words = line.split()
                    direction = words[1]
                    dimension = words[-1].split('=')
                    _, value = dimension[0], int(dimension[1])
                    folds.append((direction, value))
                else:
                    continue
        return cells, folds