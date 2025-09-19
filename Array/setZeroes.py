from typing import List


class Solution:
    def setZeroes(self, matrix):
        # check to see zeroes in first column
        zeroinFirstCol = False
        for row in range(len(matrix)):
            # if the first column is 0, set to True
            if matrix[row][0] == 0:
                zeroinFirstCol = True
            # go through each column from 1-n
            for col in range(1, len(matrix[0])):
                if matrix[row][col] == 0:
                    # mark row and column as 0
                    matrix[row][0] = 0
                    matrix[0][col] = 0
        # update the matrix in reverse order
        for row in range(len(matrix) - 1, -1, -1):
            for col in range(len(matrix[0]) - 1, 0, -1):
                # if the row or column was marked as 0, set the current cell to 0
                if matrix[row][0] == 0 or matrix[0][col] == 0:
                    matrix[row][col] = 0
            # handle first column separately
            if zeroinFirstCol:
                matrix[row][0] = 0