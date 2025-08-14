from typing import List

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        first = coordinates[0]
        second = coordinates[1]

        # if x1 and x2 are 0 (meaning the slope is undefined or a straight line upwards)
        if first[0] == second[0]:
            # go through the rest of the coordinates and ensure the line is still straight
            for i in range(2, len(coordinates)):
                if coordinates[i][0] != first[0]:
                    return False
            return True

        # calculate slope, this must be consistent in a linear syste,
        slope = (first[1] - second[1]) / (first[0] - second[0])

        # loop through all the coordinates
        for i in range(1, len(coordinates)):
            # get the coordinates before
            x1, y1 = coordinates[i-1]
            # get current coordinates
            x2, y2 = coordinates[i]

            # check to see if there is an undefined slope, if so return false since teh slope is not undefined at this point
            if x1 == x2:
                return False

            # if the slope of the current coordinates is not equal to the given slope, return false
            if (y1-y2) / (x1-x2) != slope:
                return False

        return True
