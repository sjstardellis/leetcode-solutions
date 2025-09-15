from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # binary search setup
        left = 0
        right = len(nums) - 1

        # while the two pointers have not overlapped
        while left <= right:
            # set the midpoint
            mid = (left + right) // 2

            # if the midpoint is the target, just return the midpoint
            if nums[mid] == target:
                return mid
            # if target is smaller, search left half
            elif nums[mid] > target:
                right = mid - 1
            # if target is larger, search right half
            else:
                left = mid + 1

        # if not found, left is the correct insert position
        return left