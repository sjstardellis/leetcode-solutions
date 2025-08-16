from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # keep track of the position in the list where the next element that is not equal to val should be placed
        removed = 0

        # go through entire array 0 to n-1
        for i in range(len(nums)):
            # if the value at i is not the value we want to remove, meaning the element should stay in place
            if nums[i] != val:
                # transporting the current element to the position removed is at, since that is the next valid position
                nums[removed] = nums[i]
                removed += 1

        return removed