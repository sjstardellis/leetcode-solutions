# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # stack starts with root
        stack = [root]
        # while stack is not empty
        while stack:
            # pop the top element
            node = stack.pop()
            # if the node is not null
            if node:
                # temp to store left side
                temp = node.left
                # switch left side to the right
                node.left = node.right
                # set the right side to the left
                node.right = temp
                # add both children to the stack, repeat
                stack.append(node.left)
                stack.append(node.right)

        return root
