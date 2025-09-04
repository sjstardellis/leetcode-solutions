# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        # create our two arrays of leaves
        tree1 = []
        tree2 = []
        # create our two stacks
        stack1 = [root1]
        stack2 = [root2]

        # while the stack is not empty
        while stack1:
            # pop the top node
            node = stack1.pop()
            # if the node is not null
            if node:
                # check if this node is a leaf (no left or right child)
                if not node.left and not node.right:
                    # add to the list of leaves
                    tree1.append(node.val)
                else:
                    # push right first so left gets processed first
                    # left to right traversal because of LIFO (stack)
                    stack1.append(node.right)
                    stack1.append(node.left)
        # repeat for tree2
        while stack2:
            node = stack2.pop()
            if node:
                if not node.left and not node.right:
                    tree2.append(node.val)
                else:
                    stack2.append(node.right)
                    stack2.append(node.left)
        return tree1 == tree2