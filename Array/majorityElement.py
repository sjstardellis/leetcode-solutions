from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # count of the current candidate
        count = 0
        # the current potential majority element
        candidate = 0

        # go through all the numbers
        for num in nums:
            # if the count is zero, set new candidate
            if count == 0:
                candidate = num
            # add the count if it is the candidate
            if num == candidate:
                count += 1
            # subtract the count if it isn't the candidate
            else:
                count -= 1

        return candidate