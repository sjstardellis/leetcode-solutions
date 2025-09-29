from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # index we are supposed to reach
        goal = len(nums)-1

        # go from second to last index to index 0
        for i in range(len(nums) - 2, -1, -1):
            # check to see we can reach the goal from the current index
            if i + nums[i] >= goal:
                # if so, then move goal to the current index
                goal = i
                # the for loop will move backwards one index
        # if we reach index 0, then we can make it to the goal and return true
        return True if goal == 0 else False

