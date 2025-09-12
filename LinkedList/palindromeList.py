# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # array to store our list
        arr = []

        # store all values in the array
        while head:
            arr.append(head.val)
            head = head.next
        # our two pointers
        left = 0
        right = len(arr) - 1
        # while the bounds have not intercepted
        while left < right:
            # if the values do not match, return false
            if arr[left] != arr[right]:
                return False
            # otherwise, move pointers inward
            left += 1
            right -= 1

        return True