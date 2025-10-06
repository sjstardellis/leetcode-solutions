from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # hashmap to store our seen numbers
        seen = {}
        # enumerate through each index and value
        for i, val in enumerate(nums):
            # check if the current number is already in seen and if the distance is within the limit k
            if val in seen and i - seen[val] <= k:
                return True
            else:
                # add to seen
                seen[val] = i
        # return false if for loop doesn't satisfy condition
        return False
