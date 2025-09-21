# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # root base case
        if root is None:
            return True

        # create two new roots, each side of the tree
        root1, root2 = root.left, root.right
        # the stack will keep track of the pairing
        stack = [(root1, root2)]

        while stack:
            # pop the pairing off the stack
            node1, node2 = stack.pop()
            # if both are none, then continue
            if node1 is None and node2 is None:
                continue
            # if one is none, return false
            if node1 is None or node2 is None:
                return False
            # value check
            if node1.val != node2.val:
                return False
            else:
                # add the left and right, and vice versa to the stack
                stack.append((node1.left, node2.right))
                stack.append((node1.right, node2.left))
        return True