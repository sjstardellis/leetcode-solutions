from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # allows O(1) time for checking elements and removes duplicates
        num_set = set(nums)

        # keep track of our longest sequence
        longest = 0
        # loop through the set
        for n in num_set:
            # checking to see if the previous number is not in the set
            if n-1 not in num_set:
                # if n-1 is not present, it means n is the smallest number in the current sequence
                length = 1
                # add to current sequence
                while n + length in num_set:
                    # while n + length is in the sequence, keep adding to the length
                    length += 1
                # compare which is the longest sequence
                longest = max(longest, length)

        return longest