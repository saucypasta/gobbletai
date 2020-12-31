import numpy as np

class board():
    def __init__(self):
        self.init_board = np.zeros([4,4])
        self.player = 0
        #3 is big, 1 is small
        self.pl_pieces = [[1,2,3,4],[1,2,3,4],[1,2,3,4]]
        self.p2_pieces = [[1,2,3,4],[1,2,3,4],[1,2,3,4]]
        self.current_board = self.init_board

    def valid_action(self, stack, p_row, p_col, row, col):
        pieces =  self.p1_pieces
        if self.player == 1:
            pieces = self.p2_pieces

        if stack != -1 :
            if len(pieces[stack]) == 0):
                print("No pieces in that stack")
                return
            if abs(self.current_board[row][col]) > pieces[stack][-1]:
                print("Can't gobble a bigger piece")
                return

        if abs(self.current_board[row][col]) >





    def place_piece(self, stack, piece, row, col):
        self.current_board[row][column] = piece
