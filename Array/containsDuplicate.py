from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # hash set
        seen = set()
        # going through all entries
        for num in nums:
            # if we see the current number in seen, return true that there are duplicates
            if num in seen:
                return True
            # if not in seen, add the number to the hash set
            seen.add(num)
        return False
