import numpy as np


class EightQueen():
    def __init__(self):
        self.solution_num = 0
        self.chessboard = np.zeros((8, 8))
        self.solutions = []
        self.current_row = 0

    def reset(self):
        for i in range(self.current_row, 8):
            self.chessboard[i] = np.zeros(8)

    def check(self):
        if self.current_row == 0:
            return True
        # check every column
        for i in range(8):
            if sum(self.chessboard[:, i]) > 1:
                return False

        # check every dialog
        queen_pos = []
        for i in range(self.current_row+1):
            queen_col = np.argmax(self.chessboard[i])
            queen_pos.append(np.array([i, queen_col]))

        queen_num = len(queen_pos)
        for i in range(queen_num):
            for j in range(i+1, queen_num):
                if abs(queen_pos[i][0]-queen_pos[j][0]) == abs(queen_pos[i][1]-queen_pos[j][1]):
                    return False
        return True

    def r_calculate(self):
        for i in range(8):
            self.reset()
            self.chessboard[self.current_row][i] = 1
            if self.check():
                self.current_row += 1
                if self.current_row == 8:
                    solution = self.chessboard.copy()
                    self.solutions.append(solution)
                    self.current_row -= 1
                else:
                    self.r_calculate()
        # important, go back to previous row if this row has no position for a queen
        self.current_row -= 1

    def result(self):
        self.r_calculate()
        self.solution_num = len(self.solutions)
        for i in range(self.solution_num):
            print("solution %s" % (i+1))
            print(self.solutions[i])
        print("There are %s solutions for the eight queen problem." % self.solution_num)


if __name__ == '__main__':
    Chess = EightQueen()
    Chess.result()
