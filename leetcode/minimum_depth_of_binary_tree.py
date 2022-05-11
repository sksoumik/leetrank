# https://leetcode.com/problems/minimum-depth-of-binary-tree/
# Given a binary tree, find its minimum depth.
# The minimum depth is the number of nodes along the shortest path from the
# root node down to the nearest leaf node.
# Note: A leaf is a node with no children.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root) -> int:
        """
        :param root: the root of the tree
        :return: The minimum depth of the tree.
        """
        # If the root is None, return 0
        if not root:
            return 0

        # If the root is a leaf, return 1
        if not root.left and not root.right:
            return 1

        # If the root has only one child,
        # return 1 + the minDepth of the child.
        if not root.left:
            return 1 + self.minDepth(root.right)

        if not root.right:
            return 1 + self.minDepth(root.left)

        # If the root has two children,
        # return 1 + the minDepth of the smaller child.
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))


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
