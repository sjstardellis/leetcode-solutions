# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # previous pointer is set to null (head doesn't point to anything yet), curr is the head node
        prev, curr = None, head

        # while the current node is not null
        while curr:
            # temporarily store the next node so we don’t lose access to the rest of the list
            temp = curr.next
            # sets the next node pointer to the previous node
            curr.next = prev
            # move prev forward (it now becomes the current node)
            prev = curr
            # move curr forward to the next node in the original list
            curr = temp
        # prev becomes the new head since the curr pointer will be None
        return prev