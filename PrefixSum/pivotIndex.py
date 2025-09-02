from typing import List


class Solution(object):
    def pivotIndex(self, nums: List[int]) -> int:
        # total sum is started at the max, and the left sum is at 0
        # this allows us to only have to go through the loop once
        total_sum = sum(nums)
        left_sum = 0

        for i in range(len(nums)):
            # right sum is everything except left side + current number
            right_sum = total_sum - left_sum - nums[i]

            # pivot index found
            if left_sum == right_sum:
                return i

            # update left_sum for next iteration
            left_sum += nums[i]

        return -1

        # BRUTE FORCE
        # # loop over indexes
        # for idx in range(len(nums)):
        #     # reset sums each time
        #     left_sum = 0
        #     right_sum = 0
        #
        #     # sum everything to the left of index
        #     for j in range(idx):
        #         left_sum += nums[j]
        #
        #     # sum everything to the right of index
        #     for j in range(idx + 1, len(nums)):
        #         right_sum += nums[j]
        #
        #     # check if it's a pivot
        #     if left_sum == right_sum:
        #         return idx
        #
        # # if no pivot found
        # return -1