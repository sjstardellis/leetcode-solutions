from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # base case
        if not nums:
            return 0
        # index to write at
        write_index = 1
        # 1 to n
        for i in range(1, len(nums)):
            # if the number is not equal to the number at the previous index
            if nums[i] != nums[i - 1]:
                # set the number at the write index to the current number
                nums[write_index] = nums[i]
                # move index forward
                write_index += 1
        return write_index
