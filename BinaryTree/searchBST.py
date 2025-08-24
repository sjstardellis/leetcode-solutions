# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # base case for if root is null or not
        if not root:
            return None

        # load root node and value of the node onto stack
        stack = [(root, val)]

        # while stack is not empty
        while stack:
            # take off top node/value off the stack
            node, val = stack.pop()
            # if the node value matches the value we're searching, just return the node (the rest of the tree will follow)
            if node.val == val:
                return node
            # if children are not null, add to stack
            if node.left:
                stack.append((node.left, val))
            if node.right:
                stack.append((node.right, val))
        # if node value was not found, return None
        return None

