from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # hashmap to store our results
        hashmap = {}
        # iterating through the array
        for i in range(len(nums)):
            # taking the target and the taking the number current at
            complement = target - nums[i]
            # if the complement is in the hashmap, then we have our answer and return both index
            if complement in hashmap:
                return [i, hashmap[complement]]
            # otherwise, add new hashmap entry
            hashmap[nums[i]] = i
        # return an empty list if no solution is found
        return []