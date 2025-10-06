from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # store our result
        res = []
        # sort our numbers, avoiding duplicates and triplets
        nums.sort()
        # go through each element
        for i in range(len(nums)):
            # if the check to see if the current element is a duplicate of the previous one
            # if so, then skip
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # initialize our two pointers, one always at the end
            j = i + 1
            k = len(nums) - 1
            # while the two pointers have not overlapped
            while j < k:
                # calculate the sum
                total = nums[i] + nums[j] + nums[k]
                # if the total is not 0
                if total > 0:
                    # move pointer backward
                    k -= 1
                # otherwise move other pointer forward
                elif total < 0:
                    j += 1
                else:
                    # if the sum is equal to 0, add the result to the list
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    # skip any duplicate elements
                    while nums[j] == nums[j - 1] and j < k:
                        j += 1

        return res