from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # i = pointer for the last initialized element in nums1 (index m-1)
        i = m - 1
        # j = pointer for the last element in nums2 (index n-1)
        j = n - 1
        # k = pointer for the last position in nums1 (index m+n-1)
        k = m + n - 1

        # compare elements from the back of both arrays
        # place the larger one at nums1[k], then move pointers
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                # nums1[i] is larger, put it at the end (nums1[k])
                nums1[k] = nums1[i]
                # move nums1 pointer left
                i -= 1
            else:
                # nums2[j] is larger (or equal), put it at the end
                nums1[k] = nums2[j]
                j -= 1  # move nums2 pointer left
            k -= 1  # move the placement pointer left

        # if nums2 still has elements left, copy them into nums1
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1
