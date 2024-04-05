# https://leetcode.com/problems/binary-tree-maximum-path-sum/description/

# Given the root of a binary tree, return the maximum path sum of any non-empty path.


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        # Initialize the maximum path sum to the minimum possible value
        max_sum = float("-inf")

        def helper(node):
            nonlocal max_sum

            # If the node is None, return 0
            if not node:
                return 0

            # Recursively find the maximum path sum of the left and right subtrees
            left_sum = helper(node.left)
            right_sum = helper(node.right)

            # Update the maximum path sum with the current node
            # and the maximum path sum of the left and right subtrees
            max_sum = max(max_sum, node.val + left_sum + right_sum)

            # Return the maximum path sum that includes the current node
            # and either the left or right subtree
            return max(node.val + left_sum, node.val + right_sum, 0)

        # Find the maximum path sum using the helper function
        helper(root)

        # Return the maximum path sum
        return max_sum


if __name__ == "__main__":
    # Test the solution
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    print(Solution().maxPathSum(root))  # Output: 6
