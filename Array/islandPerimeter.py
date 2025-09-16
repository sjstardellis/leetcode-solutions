from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # dimensions of the grid
        rows = len(grid)
        cols = len(grid[0])

        # counter for the perimeter
        perimeter = 0

        # iterate through each cell in the grid
        for r in range(rows):
            for c in range(cols):
                # if the cell is land (1)
                if grid[r][c] == 1:
                    # it's a perimeter if it's the top row or the cell above is water
                    if r == 0 or grid[r - 1][c] == 0:
                        perimeter += 1

                    # it's a perimeter if it's the bottom row or the cell below is water
                    if r == rows-1 or grid[r+1][c] == 0:
                        perimeter += 1

                    # it's a perimeter if it's the first column or the cell to the left is water
                    if c == 0 or grid[r][c - 1] == 0:
                        perimeter += 1

                    # it's a perimeter if it's the last column or the cell to the right is water
                    if c == cols-1 or grid[r][c+1] == 0:
                        perimeter += 1

        return perimeter