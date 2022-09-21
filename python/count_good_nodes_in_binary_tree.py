# https://leetcode.com/problems/count-good-nodes-in-binary-tree/

# Given a binary tree root, a node X in the tree is named good if 
# in the path from root to X there are no nodes with a value greater than X.
# Return the number of good nodes in the binary tree.

# Example:

# Input: root = [3,1,4,3,null,1,5]
# Output: 4
# Explanation: Nodes in blue are good.
# Root Node (3) is always a good node.
# Node 4 -> (3,4) is the maximum value in the path starting from the root.
# Node 5 -> (3,4,5) is the maximum value in the path
# Node 3 -> (3,1,3) is the maximum value in the path.

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
            
        def dfs(root, current_max):
            nonlocal count
            
            if not root:
                return

            if root.val >= current_max:
                count += 1
                current_max = root.val
            
            dfs(root.left, current_max)
            dfs(root.right, current_max)
        
        count = 0
        dfs(root, root.val)
        return count


if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.left.left = TreeNode(3)
    root.right.left = TreeNode(1)
    root.right.right = TreeNode(5)
    print(Solution().goodNodes(root))
    

 