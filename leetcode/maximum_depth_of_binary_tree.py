# https://leetcode.com/problems/maximum-depth-of-binary-tree/
# Given the root of a binary tree, return its maximum depth.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        """
        We return the maximum of the depth of the left subtree and the depth of the right subtree, plus
        one
        
        :param root: TreeNode
        :type root: TreeNode
        :return: The maximum depth of the tree.
        """
        if root is None:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1


if __name__ == "__main__":
    s = Solution()

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

    print(s.maxDepth(three))
