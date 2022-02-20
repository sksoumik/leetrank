# invert a binary tree

# Input:

#      4
#    /   \
#   2     7
#  / \   / \
# 1   3 6   9

# Output:

#      4
#    /   \
#   7     2
#  / \   / \
# 9   6 3   1


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Solution:
    # invert the binary tree
    def invertTree(self, root):
        if root is None:
            return None
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root

    # print the tree inorder
    def inorderTraversal(self, root):
        if root is None:
            return []
        return (
            self.inorderTraversal(root.left)
            + [root.value]
            + self.inorderTraversal(root.right)
        )


if __name__ == "__main__":
    s = Solution()

    four = TreeNode(4)
    two = TreeNode(2)
    seven = TreeNode(7)
    one = TreeNode(1)
    three = TreeNode(3)
    six = TreeNode(6)
    nine = TreeNode(9)

    four.left = two
    four.right = seven
    two.left = one
    two.right = three
    seven.left = six
    seven.right = nine

    print(s.inorderTraversal(four))
    print("Inverted tree: ")
    print(s.inorderTraversal(s.invertTree(four)))
