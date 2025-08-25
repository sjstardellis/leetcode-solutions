# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # if root is null, return none
        if not root:
            return None
        # if the key is less than the current value, go left, recurse
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        # if the key is less than the current value, go right, recurse
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        # key == root.val case
        else:
            # no right child, return left
            if not root.right:
                return root.left
            # no left child, return right
            if not root.left:
                return root.right

            # two children case:
            # store the right subtree in temp
            temp = root.right
            # find the left most node in the subtree until you hit null (minimum number in the subtree, could also do the opposite_
            while temp.left:
                temp = temp.left
            # temp is the leftmost node, so it cannot have a left child
            root.val = temp.val
            # now we want to delete the node we just duplicated
            # recalls deleteNode, in which we are searching for the temporary value from the right side of the replaced node
            # once we find it, we set it to None or the right child
            root.right = self.deleteNode(root.right, temp.val)
        # return new BST
        return root