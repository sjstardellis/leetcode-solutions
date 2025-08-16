from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        # add 1 to the end of the array
        digits[-1] += 1

        # loop from right to left
        for i in range(len(digits) - 1, -1, -1):
            # if the current digit is 10
            if digits[i] == 10:
                # set the current digit to 0
                digits[i] = 0
                # check to see if the current index is the first element of the array
                if i != 0:
                    # if not the first element of the array, set the digit to the left to be + 1
                    digits[i-1] = digits[i-1] + 1
                else:
                    # if we are at the front of the array and the current digit is 10 (then set to 0)
                    # then add 1 to the front of the array and exit loop at this point
                    digits = [1] + digits

        return digits