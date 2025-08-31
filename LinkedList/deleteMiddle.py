# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # if it is one node, return None
        if not head or not head.next:
            return None
        # initialize our three pointers
        prev, slow, fast = None, head, head
        # while both are not null
        while fast and fast.next:
            # move previous to the pointer right before slow
            prev = slow
            slow = slow.next
            # this will reach the end, slow will reach the middle
            fast = fast.next.next
        # if previous is not null
        if prev:
            # node reassignment
            prev.next = slow.next
        return head

        # # count the size of the list
        # current = head
        # size = 0
        # while current:
        #     size += 1
        #     current = current.next
        # # find the middle (floor)
        # middle = size // 2
        #
        # prev, current = None, head
        # # iterate through until middle has been reached
        # for _ in range(middle):
        #     prev = current
        #     current = current.next
        # # set the previous node (the one before the deleted one) to just point to the deleted one's next node
        # # this will make the current node irrelevant to the new LinkedList
        # prev.next = current.next
        #
        # return head