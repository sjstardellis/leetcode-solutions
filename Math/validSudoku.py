from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check rows
        for row in range(9):
            valid_set = set()
            for col in range(9):
                if board[row][col] != '.':
                    if board[row][col] in valid_set:
                        return False
                    valid_set.add(board[row][col])

        # check columns
        # just flip how we're iterating, columns first now
        for col in range(9):
            valid_set = set()
            for row in range(9):
                if board[row][col] != '.':
                    if board[row][col] in valid_set:
                        return False
                    valid_set.add(board[row][col])

        # check 3x3 squares
        # 9 squares, move three indices each time
        for start_row in range(0, 9, 3):
            for start_col in range(0, 9, 3):
                # now we're starting to keep track our square
                valid_set = set()
                # go through 3 rows
                for row in range(start_row, start_row + 3):
                    # go through 3 columns
                    for col in range(start_col, start_col + 3):
                        # if it is a number
                        if board[row][col] != '.':
                            # check to see if there is a duplicate or not
                            if board[row][col] in valid_set:
                                return False
                            # otherwise add to set
                            valid_set.add(board[row][col])

        return True
