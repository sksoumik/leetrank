# https://leetcode.com/problems/merge-two-binary-trees

# You are given two binary trees root1 and root2.

# Imagine that when you put one of them to cover the other,
#  some nodes of the two trees are overlapped while the others are not. 
#  You need to merge the two trees into a new binary tree. 
#  The merge rule is that if two nodes overlap, then sum node values up as 
#  the new value of the merged node. Otherwise, the NOT 
#  null node will be used as the node of the new tree.

# Return the merged tree.

# Note: The merging process must start from the root nodes of both trees.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def mergeTrees(self, root1, root2):
        # This is a base case. If both root1 and root2 are None, then we return None.
        if not root1 and not root2:
            return None
        if not root1:
            return root2
        if not root2:
            return root1
        # This is the recursive step. We are creating a new node with the sum of the values of the two
        # nodes.
        # Then we are recursively calling the function on the left and right nodes of the two trees.
        root = TreeNode(root1.val + root2.val)
        root.left = self.mergeTrees(root1.left, root2.left)
        root.right = self.mergeTrees(root1.right, root2.right)
        return root


if __name__ == "__main__":
    # Creating a tree with root node 1, left node 3, right node 2, left.left node 5, and right.right
    # node 9.
    root1 = TreeNode(1)
    root1.left = TreeNode(3)
    root1.right = TreeNode(2)
    root1.left.left = TreeNode(5)
    root1.right.right = TreeNode(9)

    # Creating a tree with root node 2, left node 1, right node 3, left.right node 4, and right.right
    # node 7.
    root2 = TreeNode(2)
    root2.left = TreeNode(1)
    root2.right = TreeNode(3)
    root2.left.right = TreeNode(4)
    root2.right.right = TreeNode(7)

    solution = Solution()
    root = solution.mergeTrees(root1, root2)
    print(root.val)
    print(root.left.val)
    print(root.right.val)
    print(root.left.left.val)
    print(root.right.right.val)
        



        