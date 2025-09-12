# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # two pointers to help keep track when we delete
        prev, curr = None, head
        # store our seen values
        seen = set()
        # while not at the end of the list
        while curr:
            # if the current value is seen, skip the current node
            if curr.val in seen:
                prev.next = curr.next
            else:
                # otherwise, add the current to the set and move previous pointer forward
                seen.add(curr.val)
                prev = curr
            # move current pointer forward
            curr = curr.next

        return head