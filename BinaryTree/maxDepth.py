from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # base case
        if root is None:
            return 0
        # (node, current depth), start out with root node at depth 1
        stack = [(root, 1)]

        max_depth = 0
        # while the stack is not empty
        while stack:
            # pop the top of the stack and check the left/right node
            node, depth = stack.pop()
            # compare the max_depth with the current depth
            max_depth = max(max_depth, depth)
            # if the right/left side exists, add the node and depth to the stack
            if node.left:
                stack.append((node.left, depth + 1))
            if node.right:
                stack.append((node.right, depth + 1))
        # return max_depth once loop closes
        return max_depth
