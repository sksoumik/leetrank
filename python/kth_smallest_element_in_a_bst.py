# https://leetcode.com/problems/kth-smallest-element-in-a-bst/

# Given the root of a binary search tree, and an integer k,
# return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

# Example 1:
# Input: root = [3,1,4,null,2], k = 1
# Output: 1

# Example 2:
# Input: root = [5,3,6,2,4,null,null,1], k = 3
# Output: 3

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # all tree items in a list
        output = self.inorder(root)

        # sort the list in asceding order
        output.sort()

        # delete duplicate elements
        output = list(set(output))

        # return the k-1 item form the asceding order list
        return output.pop(k - 1)  # -1 because it's 1 indexed

    def inorder(self, root):
        if not root:
            return []

        return self.inorder(root.left) + [root.val] + self.inorder(root.right)


if __name__ == "__main__":
    # Example 1
    root = TreeNode(3)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.left.right = TreeNode(2)
    k = 2
    print(Solution().kthSmallest(root, k))  # 2

    # Example 2
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(6)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.left.left.left = TreeNode(1)
    k = 3
    print(Solution().kthSmallest(root, k))  # 3
