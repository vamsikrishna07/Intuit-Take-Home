import numpy as np
class MessageDecoder:
    def decode(self, matrix, index):
        for row in matrix:
            print(row)
            matrix = np.array(matrix)
            filename = "output-"+str(index)+".txt"
            np.savetxt(filename, matrix, fmt='%s', delimiter=',')
            print(f"Message saved to {filename}")