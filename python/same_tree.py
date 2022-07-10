# https://leetcode.com/problems/same-tree/
# Given the roots of two binary trees p and q, write a function to check if they are the same or not.
# Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p, q):
        """
        If p and q are both None, then they are the same tree. If one of them is None, then they are not
        the same tree. If both of them are not None, then they are the same tree if and only if their
        values are the same and their left subtrees are the same and their right subtrees are the same
        
        :param p: the root node of the first tree
        :param q: the root of the second tree
        :return: True or False
        """
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


if __name__ == "__main__":
    p = TreeNode(1)
    p.left = TreeNode(2)
    p.right = TreeNode(3)
    q = TreeNode(1)
    q.left = TreeNode(2)
    q.right = TreeNode(3)
    s = Solution()
    print(s.isSameTree(p, q))
