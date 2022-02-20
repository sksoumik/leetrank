# print binary search tree in preorder, inorder, postorder
# https://youtu.be/xo41NfT8218


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    

class Solution:
    def inorderTraversal(self, root):
        if root is None:
            return []
        return (
            self.inorderTraversal(root.left)
            + [root.value]
            + self.inorderTraversal(root.right)
        )
    
    def preorderTraversal(self, root):
        if root is None:
            return []
        return [root.value] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)
    
    def postorderTraversal(self, root):
        if root is None:
            return []
        return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.value]


if __name__ == "__main__":

    
    s = Solution()
    one = TreeNode(1)
    two = TreeNode(2)
    three = TreeNode(3)

    one.left = None
    one.right = two
    one.right.left = three
    one.right.right = None
    print(s.inorderTraversal(one))
    print(s.preorderTraversal(one))
    print(s.postorderTraversal(one))

