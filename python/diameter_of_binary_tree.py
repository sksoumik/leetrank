# https://leetcode.com/problems/diameter-of-binary-tree

# Given the root of a binary tree, return the length of the diameter of the tree.

# The diameter of a binary tree is the length of the longest path between any two nodes
# in a tree. This path may or may not pass through the root.

# The length of a path between two nodes is represented by the number of edges between them.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root):
        """
        The diameter of a binary tree is the maximum of the following three numbers:

        1. The diameter of the left subtree.
        2. The diameter of the right subtree.
        3. The longest path between any two nodes in the left subtree + the longest path between any two
        nodes in the right subtree

        :param root: the root of the tree
        :return: The diameter of the tree.
        """
        if root is None:
            return 0
        return max(
            self.diameterOfBinaryTree(root.left),
            self.diameterOfBinaryTree(root.right),
            self.maxDepth(root.left) + self.maxDepth(root.right),
        )

    def maxDepth(self, root):
        """
        The maximum depth of a binary tree is the maximum number of nodes along the path from the root
        node down to the farthest leaf node

        :param root: the root node of the tree
        :return: The max depth of the tree.
        """
        if root is None:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1


if __name__ == "__main__":
    three = TreeNode(3)
    nine = TreeNode(9)
    twenty = TreeNode(20)
    fifteen = TreeNode(15)
    seven = TreeNode(7)

    three.left = nine
    nine.left = None
    nine.right = None
    three.right = twenty
    twenty.left = fifteen
    twenty.right = seven

    s = Solution()
    print(s.diameterOfBinaryTree(three))
