# https://leetcode.com/problems/binary-tree-right-side-view

# Given the root of a binary tree, imagine yourself standing on the right side of it,
# return the values of the nodes you can see ordered from top to bottom.


# Example 1
# Input: root = [1,2,3,null,5,null,4]
# Output: [1,3,4]


# Example 2:
# Input: root = [1,null,3]
# Output: [1,3]

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # time complexity: O(n)
    # space complexity: O(n)
    # using BFS
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        queue = [root]
        result = []

        while queue:
            result.append(queue[-1].val)

            for _ in range(len(queue)):
                # remove the leftmost element from queue
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return result

    # second approach
    # time complexity: O(n^2)
    def rightSideView(self, root):
        if not root:
            return []
        right = self.rightSideView(root.right)
        left = self.rightSideView(root.left)
        return [root.val] + right + left[len(right) :]


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(4)

    print(Solution().rightSideView(root))
