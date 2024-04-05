# https://leetcode.com/problems/minimum-depth-of-binary-tree/
# Given a binary tree, find its minimum depth.
# The minimum depth is the number of nodes along the shortest path from the
# root node down to the nearest leaf node.
# Note: A leaf is a node with no children.

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:

        # if the tree is empty
        if root is None:
            return 0

        # id there is no left and right subtree
        if root.left is None and root.right is None:
            return 1

        # if there is no left subtree
        if root.left is None:
            return self.minDepth(root.right) + 1

        # if there is no right subtree
        if root.right is None:
            return self.minDepth(root.left) + 1

        # if left and right subtree both exists
        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1


# main function
if __name__ == "__main__":
    # create a binary tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)

    # create a solution
    sol = Solution()

    # print the minimum depth of the binary tree
    print(sol.minDepth(root))
