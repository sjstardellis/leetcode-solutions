from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # result number
        result = 0
        # going through all the entries
        for num in nums:
            # our result should be the only number not canceled out from the XOR operations
            result = result^num
        return result

        # # seen hashmap to mark what we've seen
        # seen = {}
        # # iterate through the hashmap, adding the entries
        # for num in nums:
        #     seen[num] = seen.get(num, 0) + 1
        #
        # # going through the key value pairs of the hashmap
        # for num, count in seen.items():
        #     if count == 1:
        #         return num
