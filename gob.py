import numpy as np

class board():
    def __init__(self):
        self.init_board = self.init_board()
        #player1 is 1, player 2 is -1
        self.player = 1
        #4 is big, 1 is small
        self.pl_pieces = [[1,2,3,4],[1,2,3,4],[1,2,3,4]]
        self.p2_pieces = [[1,2,3,4],[1,2,3,4],[1,2,3,4]]
        self.current_board = self.init_board

    def init_board(self):
        board = []
        for i in range(0,4):
            row  = []
            for j in range(0,4):
                row.append([])
            board.append(row)

    def three_in_row(self, row, col):
        rsum = 0
        csum = 0
        dsum = 0
        sign = self.player * -1
        board = self.current_board
        for r in board:
            for c in board:
                if c != []:
                    c = c* sign

        for i in range(0,4):
            loc = board[row][i]
            if len(loc) != 0 and loc[-1] > 0:
                rsum += 1

            loc = board[i][col]
            if len(loc) != 0 and loc[-1] > 0:
                csum += 1

            loc = board[i][i]
            if row == col and len(loc) != 0 and loc[-1] > 0:
                dsum +=1
            loc = board[i][3-i]
            if row == 3 - col and len(loc) != 0 and loc[-1] > 0:
                dsum +=1

        if rsum == 3 or csum == 3 or dsum == 3:
            return True
        return False

    def is_opponent(self, row, col):
        sign = self.player * -1
        loc = self.current_board[row][col]
        if len(loc) == 0:
            return False
        if loc[-1]/loc[-1] == self.player:
            return False
        return True


    def valid_action(self, stack, p_row, p_col, row, col):
        pieces =  self.p1_pieces
        start_loc = self.current_board[p_row][p_col]
        end_loc = self.current_board[row][col]
        if self.player == 1:
            pieces = self.p2_pieces

        if stack != -1 :
            if len(pieces[stack]) == 0):
                print("No pieces in that stack")
                return False
            if len(end_loc) != 0 and abs(end_loc[-1]) > pieces[stack][-1]:
                print("Can't gobble a bigger piece")
                return False
            if is_opponent(row, col) and not self.three_in_row(row,col):
                print("Can't gobble unless 3 in a row")
                return False

        if len(start_loc) == 0:
            print("No piece to move")
            return False

        if len(end_loc) != 0:
            if abs(start_loc) < abs(end_loc[-1]):
                print("Can't gobble a bigger piece")
                return False
        return True



    def place_piece(self, stack, prow, pcol, row, col):
        piece = 0
        if valid_action(stack, prow, pcol, row, col):
            if stack != -1:
                if self.player == 1:
                    piece = self.p1_pieces[stack].pop()
                else:
                    piece = self.p2_pieces[stack].pop()
            else:
                piece = self.current_board[prow][pcol].pop()
        self.current_board[row][column].append(piece)

    #-1 means player2 won, 1 means player1 won, 0 means no win
    def won(self):
        for i in range(0,4):
            sum = 0
            loc = self.current_board[i][0]
            if len(loc == 0):
                continue
            sign = loc/abs(loc)
            for j in range(0,4):
                loc = self.current_board[i][j]
                if len(loc) == 0:
                    break
                if loc == self.player:
                    sum += 1
            if sum == 4:
                return True

        for i in range(0,4):
            sum = 0
            loc = self.current_board[0][i]
            if len(loc == 0):
                continue
            sign = loc/abs(loc)
            for j in range(0,4):
                loc = self.current_board[i][j]
                if len(loc) == 0:
                    break
                if loc == self.player:
                    sum += 1
            if sum == 4:
                return True
