from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxCount = 0 # keep track of the overall max
        currentMax = 0 # keep track in the loop

        # loop through all the numbers
        for num in nums:
            # if the current number is 1
            if num == 1:
                # add to the current max
                currentMax += 1
                # check to see if it is greater than the overall max
                maxCount = max(maxCount, currentMax)
            else:
                # reset currentMax count
                currentMax = 0
        return maxCount
