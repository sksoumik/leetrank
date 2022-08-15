# https://leetcode.com/problems/two-sum-iv-input-is-a-bst

# Given the root of a Binary Search Tree and a target number k, return true if there 
# exist two elements in the BST such that their sum is equal to the given target.

# Example 1:
# Input: root = [5,3,6,2,4,null,7], k = 9
# Output: true
# Explanation: 5 and 4

# Example 2:
# Input: root = [5,3,6,2,4,null,7], k = 28
# Output: false

from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        # use a hash table to store the values in the BST
        hash_table = {}
        return self.findTargetHelper(root, k, hash_table)

    
    def findTargetHelper(self, root: Optional[TreeNode], k: int, hash_table: dict) -> bool:
        if not root:
            return False

        complement = k - root.val
        if complement in hash_table:
            return True
        hash_table[root.val] = True
        return (
            self.findTargetHelper(root.left, k, hash_table) or 
            self.findTargetHelper(root.right, k, hash_table)
        )
        


if __name__ == '__main__':
    obj = Solution()
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(6)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.right.right = TreeNode(7)
    print(obj.findTarget(root, 9))
    print(obj.findTarget(root, 28))
    