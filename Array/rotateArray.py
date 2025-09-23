from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n
        # reverse the list
        nums.reverse()
        # grab the last k numbers and reverse them
        nums[:k] = reversed(nums[:k])
        # reverse the rest of the list
        nums[k:] = reversed(nums[k:])