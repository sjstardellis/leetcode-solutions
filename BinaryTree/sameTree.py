# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # a stack for each tree
        stack1 = [p]
        stack2 = [q]
        # while both stacks are not empty
        while stack1 and stack2:
            # take the first item off the stack
            node1 = stack1.pop()
            node2 = stack2.pop()
            # if null both are null, continue
            if not node1 and not node2:
                continue
            # if one is null, then return false
            if not node1 or not node2:
                return False
            # if the values do not match, return false
            if node1.val != node2.val:
                return False

            # add both children
            stack1.append(node1.left)
            stack1.append(node1.right)
            stack2.append(node2.left)
            stack2.append(node2.right)
        # if both stacks are empty, the trees are identical
        return not stack1 and not stack2

