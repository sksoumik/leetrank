// https://leetcode.com/problems/diameter-of-binary-tree

// Given the root of a binary tree, return the length of the diameter of the tree.

// The diameter of a binary tree is the length of the longest path between any two nodes
// in a tree. This path may or may not pass through the root.
// The length of a path between two nodes is represented by the number of edges between them.

function TreeNode(val, left, right) {
  this.val = val === undefined ? 0 : val;
  this.left = left === undefined ? null : left;
  this.right = right === undefined ? null : right;
}

var diameterOfBinaryTree = function (root) {
  if (!root) return 0;

  return Math.max(
    diameterOfBinaryTree(root.left),
    diameterOfBinaryTree(root.right),
    maxDepth(root.left) + maxDepth(root.right)
  );
};

var maxDepth = function (root) {
  if (!root) return 0;
  return Math.max(maxDepth(root.left), maxDepth(root.right)) + 1;
};

console.log(
  diameterOfBinaryTree(new TreeNode(1, new TreeNode(2), new TreeNode(3)))
);
