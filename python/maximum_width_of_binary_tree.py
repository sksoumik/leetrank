# https://leetcode.com/problems/maximum-width-of-binary-tree

# Given the root of a binary tree, return the maximum width of the given tree.

# Example 1:
# Input: root = [1,3,2,5,3,null,9]
# Output: 4
# Explanation: The maximum width exists in the third level with length 4 (5,3,null,9).

# Example 2:
# Input: root = [1,3,2,5,null,null,9,6,null,7]
# Output: 7
# Explanation: The maximum width exists in the fourth level with length 7 (6,null,null,null,null,null,7).

# vid: https://youtu.be/673DsIXOkWg

from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # time complexity is O(n), where n is number of nodes, 
    # because we traverse our tree, using bfs. Space complexity is O(w), 
    # where w is the biggest number of nodes in level, because we need to keep our queue
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        # we will keep the node and its index in the queue
        queue = [(root, 0)]
        max_width = 0
        while queue:
            # The `queue` is a list of tuples, where each tuple is a node and its index. The index is
            # the position of the node in the tree. The `max_width` is the maximum difference between
            # the indices of the leftmost and rightmost nodes in the queue.
            # rightmost index - leftmost index + 1
            max_width = max(max_width, queue[-1][1] - queue[0][1] + 1)  
            # [(root, 0)]  -1 is the rightmost node, 0 is the leftmost node
            # and index is placed in the tuple as the second element, so 1
            for _ in range(len(queue)):
                # we remove the first element from the queue
                # it will return a tuple (node, index)
                node, index = queue.pop(0)
                # we add the left child to the queue and we update its index
                if node.left:
                    queue.append((node.left, 2 * index))
                # we add the right child to the queue and we update its index
                if node.right:
                    queue.append((node.right, 2 * index + 1))
        return max_width

if __name__ == "__main__":
    sol = Solution()

    root = TreeNode(1, TreeNode(3, TreeNode(5), TreeNode(3)), TreeNode(2, None, TreeNode(9)))
    print(sol.widthOfBinaryTree(root))

    