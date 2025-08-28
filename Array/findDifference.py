from typing import List

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        # create sets out of the two arrays
        set1, set2 = set(nums1), set(nums2)
        # set1 - set2 gives elements in nums1 but not in nums2
        # set2 - set1 gives elements in nums2 but not in nums1
        return [list(set1 - set2), list(set2 - set1)]
