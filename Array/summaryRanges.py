from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        # resultant array
        res = []
        # if null, just return empty array
        if not nums:
            return res
        # initialize start and end range
        start = nums[0]
        end = nums[0]

        # iterate through the numbers starting from the second element
        for n in nums[1:]:
            # if the next number is consecutive, add to the range
            if n == end + 1:
                end = n
            else:
                # if the sequence breaks
                if start == end:
                    # range is just one number
                    res.append(str(start))
                else:
                    # append start and end
                    res.append(str(start) + "->" + str(end))
                # set start and end at n
                start = n
                end = n
        # get the last number range
        # just one number
        if start == end:
            res.append(str(start))
        else:
            # last number of the range, is consecutive
            res.append(str(start) + "->" + str(end))
        return res