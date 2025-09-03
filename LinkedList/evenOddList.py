# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        # if the list is empty or has only one node
        if not head or not head.next:
            return head

        # initialize our heads, odd is always first and even is always second
        odd, even = head, head.next
        # store the start of the even head
        even_head = even

        # while there is an even and odd node existing
        while even and even.next:
            # link current odd node to the next odd node (skip the even one)
            odd.next = even.next
            # move odd pointer
            odd = odd.next
            # link current even node to the next even node (skip the odd we just used)
            even.next = even.next.next
            # move even pointer forward
            even = even.next

        # connect the end of the odd list to the head of the even list
        odd.next = even_head

        return head