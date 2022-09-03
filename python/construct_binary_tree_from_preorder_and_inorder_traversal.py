# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

# Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and
# inorder is the inorder traversal of the same tree, construct and return the binary tree.


# Example 1:
# Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
# Output: [3,9,20,null,null,15,7]

# Example 2:
# Input: preorder = [-1], inorder = [-1]
# Output: [-1]


from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # how to construct BST: https://youtu.be/PoBGyrIWisE
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # The root of the subtree will always be the first element in preorder.
        # to construct the left subtree, we take all the nodes to the left of the root value (from inorder)
        # to construct the right subtree, we take all the nodes to the right of the root (from inoder)

        if not preorder or not inorder:
            return None

        # root index for our BST
        root_index = inorder.index(preorder.pop(0))

        root = TreeNode(inorder[root_index])

        # left subtree
        root.left = self.buildTree(preorder, inorder[0:root_index])

        # right subtree
        root.right = self.buildTree(preorder, inorder[root_index + 1 :])
        return root 

    # print tree in preorder traverse
    def printTree(self, root: Optional[TreeNode]) -> None:
        if root:
            print(root.val)
            self.printTree(root.left)
            self.printTree(root.right)


if __name__ == "__main__":
    solution = Solution()
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    root = solution.buildTree(preorder, inorder)
    solution.printTree(root)
