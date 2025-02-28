from InputParser import InputParser
from MatrixBuilder import MatrixBuilder
from MatrixFolder import MatrixFolder
from MessageDecoder import MessageDecoder

class ActivityManager:
    def __init__(self, file_path, index):
        self.file_path = file_path
        self.input_parser = InputParser(file_path=file_path)
        self.matrix_buider = MatrixBuilder()
        self.matrix_folder = MatrixFolder()
        self.message_decoder = MessageDecoder()
        self.index = index

    def start(self):
        cells, folds = self.input_parser.parse()
        cells = self.matrix_folder.apply_folds(cells=cells, folds=folds)
        matrix = self.matrix_buider.build_matrix(cells=cells)
        self.message_decoder.decode(matrix, self.index) 