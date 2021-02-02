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

    def calculate(self):
        for q1 in range(8):
            self.current_row = 0
            self.reset()
            self.chessboard[self.current_row][q1] = 1
            for q2 in range(8):
                self.current_row = 1
                self.reset()
                self.chessboard[self.current_row][q2] = 1
                if not self.check():
                    continue
                for q3 in range(8):
                    self.current_row = 2
                    self.reset()
                    self.chessboard[self.current_row][q3] = 1
                    if not self.check():
                        continue
                    for q4 in range(8):
                        self.current_row = 3
                        self.reset()
                        self.chessboard[self.current_row][q4] = 1
                        if not self.check():
                            continue
                        for q5 in range(8):
                            self.current_row = 4
                            self.reset()
                            self.chessboard[self.current_row][q5] = 1
                            if not self.check():
                                continue
                            for q6 in range(8):
                                self.current_row = 5
                                self.reset()
                                self.chessboard[self.current_row][q6] = 1
                                if not self.check():
                                    continue
                                for q7 in range(8):
                                    self.current_row = 6
                                    self.reset()
                                    self.chessboard[self.current_row][q7] = 1
                                    if not self.check():
                                        continue
                                    for q8 in range(8):
                                        self.current_row = 7
                                        self.reset()
                                        self.chessboard[self.current_row][q8] = 1
                                        if self.check():
                                            # need to copy the class attribute chessboard,
                                            # because it changes while calculate
                                            solution = self.chessboard.copy()
                                            self.solutions.append(solution)
                                        else:
                                            continue

    def result(self):
        self.calculate()
        self.solution_num = len(self.solutions)
        print("There are %s solutions for the eight_queen problem." % self.solution_num)
        for i in range(self.solution_num):
            print("solution %s" % (i+1))
            print(self.solutions[i])


if __name__ == '__main__':
    Chess = EightQueen()
    Chess.result()
