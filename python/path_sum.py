# https://leetcode.com/problems/path-sum

# Given the root of a binary tree and an integer targetSum, return true if the tree has a
# root-to-leaf path such that adding up all the values along the path equals targetSum.

# A leaf is a node with no children.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root, targetSum) -> bool:
        """
        :param root: TreeNode
        :type root: TreeNode
        :param targetSum: int
        :type targetSum: int
        :return: bool
        """
        # if the tree has no root
        if root is None:
            return False

        # if the root has no left or right leaf
        # means we only have root val
        if root.left is None and root.right is None:
            return root.val == targetSum

        # if we have left or right leafs
        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(
            root.right, targetSum - root.val
        )


if __name__ == "__main__":
    # make a tree
    three = TreeNode(3)
    nine = TreeNode(9)
    twenty = TreeNode(20)
    fifteen = TreeNode(15)
    seven = TreeNode(7)

    three.left = nine
    three.right = None
    nine.left = twenty
    nine.right = None
    twenty.left = None
    twenty.right = seven

    s = Solution()
    print(s.hasPathSum(three, 18))
    print(s.hasPathSum(three, 17))
    print(s.hasPathSum(three, 39))
