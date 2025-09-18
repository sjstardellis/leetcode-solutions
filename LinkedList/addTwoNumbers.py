# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # dummy head
        dummy = ListNode()
        # resultant list
        res = dummy
        # total is the running sum, carry keeps leftover for the next digit
        total = carry = 0

        # keep looping while there are digits left in l1, l2, or carry
        while l1 or l2 or carry:
            # start with whatever carry is left over
            total = carry
            # if l1 node still exits
            if l1:
                # add to the total and move forward
                total += l1.val
                l1 = l1.next
            # if l2 node still exits
            if l2:
                # add to the total and move forward
                total += l2.val
                l2 = l2.next
            # digit for the new node
            num = total % 10 # remainder
            carry = total // 10 # carry for next digit

            # attach the new digit node to the result list
            dummy.next = ListNode(num)
            # move dummy pointer forward
            dummy = dummy.next

        # return the built list, skipping the dummy head
        return res.next