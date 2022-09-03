# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

# Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes
# p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”


# Example 1:
# Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
# Output: 6
# Explanation: The LCA of nodes 2 and 8 is 6.

# Example 2:
# Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
# Output: 2
# Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.

# Example 3:
# Input: root = [2,1], p = 2, q = 1
# Output: 2


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lowestCommonAncestor(
        self, root: TreeNode, p: TreeNode, q: TreeNode
    ) -> TreeNode:
        # if p and q are both smaller than root, they are in the left subtree
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)

        # if p and q are both greater than root, they are in the right subtree
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)

        # otherwise, they are on different sides (or equal) and the root is LCA
        return root


if __name__ == "__main__":
    # Example 1
    root = TreeNode(6)
    root.left = TreeNode(2)
    root.right = TreeNode(8)
    root.left.left = TreeNode(0)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(7)
    root.right.right = TreeNode(9)
    root.left.right.left = TreeNode(3)
    root.left.right.right = TreeNode(5)
    p = TreeNode(2)
    q = TreeNode(8)
    print(Solution().lowestCommonAncestor(root, p, q).val)  # 6

    # Example 2
    root = TreeNode(6)
    root.left = TreeNode(2)
    root.right = TreeNode(8)
    root.left.left = TreeNode(0)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(7)
    root.right.right = TreeNode(9)
    root.left.right.left = TreeNode(3)
    root.left.right.right = TreeNode(5)
    p = TreeNode(2)
    q = TreeNode(4)
    print(Solution().lowestCommonAncestor(root, p, q).val)  # 2

    # Example 3
    root = TreeNode(2)
    root.left = TreeNode(1)
    p = TreeNode(2)
    q = TreeNode(1)
    print(Solution().lowestCommonAncestor(root, p, q).val)  # 2
