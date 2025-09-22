# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy

        # while both lists are not null
        while list1 and list2:
            # if the node in list1 is greater than list2
            if list1.val > list2.val:
                # the next node is list2 node and move it forward
                cur.next = list2
                list2 = list2.next
            else:
                # if the node in list2 is greater than list1
                cur.next = list1
                # the next node is list1 node and move it forward
                list1 = list1.next
            # move the pointer up to the new node
            cur = cur.next
        # attach the rest of the non-empty list
        if list1:
            cur.next = list1
        else:
            cur.next = list2
        # skip dummy head, returns new list
        return dummy.next