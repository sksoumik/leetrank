# https://leetcode.com/problems/subtree-of-another-tree/

# Given the roots of two binary trees root and subRoot,
# return true if there is a subtree of root with the same structure
# and node values of subRoot and false otherwise.

# A subtree of a binary tree tree is a tree that consists of a node in
# tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.


# Example 1:
# Input: root = [3,4,5,1,2], subRoot = [4,1,2]
# Output: true

# Example 2:
# Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
# Output: false

# video explanation: https://youtu.be/E36O5SWp-LE

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # time complexity: O(len(root) * len(subRoot))
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # if the subRoot is empty, then it is a subtree of root
        # return True
        if subRoot is None:
            return True

        # if the root is empty, then it is not a subtree of subRoot
        # return False
        if root is None:
            return False

        # if the root and subRoot are the same tree, then return True
        if self.isSameTree(root, subRoot):
            return True

        # if the root and subRoot are not the same tree, then check the left and right subtree
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSameTree(self, p, q):
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        if p.val != q.val:
            return False
        # when same tree, return True, else return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
