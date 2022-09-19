# https://leetcode.com/problems/binary-tree-level-order-traversal

# Given the root of a binary tree, return the level order traversal
# of its nodes' values. (i.e., from left to right, level by level).


# Example
# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[9,20],[15,7]]

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # time complexity: O(n)
    # space complexity: O(n)
    # explanation: see the origial level order traversal from dsa/tree_traversal.py
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = []
        level = []
        result = []

        if root:
            queue.append(root)

        while queue:
            for _ in range(len(queue)):
                node = queue.pop(0)
                level.append(node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            result.append(level)
            level = []

        return result


if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    print(Solution().levelOrder(root))
