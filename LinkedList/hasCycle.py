# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        slow, fast = head, head
        # while fast and fast.next are not null
        while fast and fast.next:
            # move fast twice
            fast = fast.next.next
            # move slowo once
            slow = slow.next
            # if they are lined up, return true for a cycle
            if fast == slow:
                return True
        return False