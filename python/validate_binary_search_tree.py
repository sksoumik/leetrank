# https://leetcode.com/validate-binary-search-tree

# Given the root of a binary tree, determine if it is a valid binary search tree (BST).

# A valid BST is defined as follows:

# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # time complexity: O(n) where n is the number of nodes in the tree
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        output = self.inorder(root)

        for i in range(1, len(output)):
            if output[i] <= output[i - 1]:
                return False

        return True

    # inorder traversal returns all the tree nodes in inorder
    # nodes will be returned in a list
    def inorder(self, root: Optional[TreeNode]):
        if not root:
            return []

        return self.inorder(root.left) + [root.val] + self.inorder(root.right)
