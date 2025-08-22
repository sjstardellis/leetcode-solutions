from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # keep track of the index
        index = 0

        for i in range(len(nums)):
            # this part moves all the non-zero to the front of the array
            if nums[i] != 0:
                # places the non-zero number into the position pointed to by index
                nums[index] = nums[i]
                # the next non-zero number should be placed at the next slot
                index = index + 1

        # now we will have some duplicate numbers but the index is keeping track of the range from index to the end of the array to be zero
        for i in range(index, len(nums)):
            # set the range to all 0s
            nums[i] = 0


        # count = 0
        # for num in nums:
        #     if num == 0:
        #         count += 1
        #         nums.remove(num)
        # for i in range(count):
        #     nums.append(0)