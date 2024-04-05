# https://leetcode.com/problems/symmetric-tree

# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root):
        if root is None:
            return True
        return self.isMirror(root.left, root.right)

    def isMirror(self, left, right):
        # if the left subtree is empty and right subtree is empty
        if left is None and right is None:
            return True
        # if one is empty and another is not
        if left is None or right is None:
            return False

        return (
            # first check if the root of left subtree and right subtree is same
            left.val == right.val
            and
            # then we check, left subtree's left node should be equal to right subtree's right node
            self.isMirror(left.left, right.right)
            and
            # then we check, left subtree's right node should be equal to right subtree's left node
            self.isMirror(left.right, right.left)
        )


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(3)
    print(Solution().isSymmetric(root))
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)
    print(Solution().isSymmetric(root))
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(4)
    print(Solution().isSymmetric(root))
