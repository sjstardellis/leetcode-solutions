# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # base case
        if not root:
            return False

        # storing node and remaining sum
        stack = [(root, targetSum-root.val)]

        # while stack isn't empty
        while stack:
            # pop the current node and the remaining sum
            node, remaining_sum = stack.pop()

            # check to see if there are no children and the remaining sum is 0
            if not node.left and not node.right and remaining_sum == 0:
                return True

            # if a left child exists, push it onto the stack with the updated remaining sum.
            if node.left:
                stack.append((node.left, remaining_sum-node.left.val))
            if node.right:
                stack.append((node.right, remaining_sum-node.right.val))

        # if the stack is empty and no condition is met, return false
        return False
