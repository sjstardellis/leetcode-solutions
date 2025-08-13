from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # left and right boundaries
        left, right = 0, len(nums) - 1
        while left <= right:
            # calculating the middle every time
            mid = (left + right) // 2
            # if target is found case
            if nums[mid] == target:
                return mid
            # if the mid is less than the target, we want to set the middle as the new left (+1 to avoid checking same number)
            elif nums[mid] < target:
                left = mid + 1
            # if the mid is greater than the target, we want to set the middle as the new right (-1 to avoid checking same number)
            else:
                right = mid - 1
        # return -1 if target not found
        return -1