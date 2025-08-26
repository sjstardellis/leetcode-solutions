from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # get the sum from beginning to k
        s = sum(nums[:k])
        # set the max to be m (no need to divide yet, since the greatest sum will be the max and k stays constant)
        maximum = s
        # loop through from k to n since we don't want to overflow
        for i in range(k, len(nums)):
            # take the current sum and add:
            # take the current number at i (new number) and have the old number (i-k) subtract it
            # it will account for the change of the sum
            s += nums[i] - nums[i-k]
            # if the current sum is greater than the previous sum, then set the new sum to s
            if s > maximum:
                maximum = s
        return maximum / float(k)


        # BRUTE FORCE
        # if k == 1:
        #     return max(nums)
        # count = 0
        # read = 0
        # sub_array = []
        # current_max = float("-inf")
        # while read < len(nums)-k+1:
        #     while count != k:
        #         sub_array.append(nums[read+count])
        #         count += 1
        #     current_max = max(current_max, sum(sub_array)/len(sub_array))
        #     read += 1
        #     count = 0
        #     sub_array = []
        # return current_max