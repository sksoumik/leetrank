# https://leetcode.com/problems/binary-tree-inorder-traversal/

# Given the root of a binary tree, return the inorder traversal of its nodes' values.

from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root):
        if root is None:
            return []
        return (
            self.inorderTraversal(root.left)
            + [root.val]
            + self.inorderTraversal(root.right)
        )


if __name__ == "__main__":
    s = Solution()
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)

    n1.left = None
    n1.right = n2
    n1.right.left = n3
    n1.right.right = None
    print(s.inorderTraversal(n1))
