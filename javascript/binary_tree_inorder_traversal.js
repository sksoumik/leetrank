// https://leetcode.com/problems/binary-tree-inorder-traversal/

// Given the root of a binary tree, return the inorder traversal of its nodes' values.

function TreeNode(val, left, right) {
  this.val = val === undefined ? 0 : val;
  this.left = left === undefined ? null : left;
  this.right = right === undefined ? null : right;
}

var inorderTraversal = function (root) {
  // if root is null, return an empty array
  if (!root) return [];
  // if root is not null, return the inorder traversal of the left subtree
  // concatenated with the root's value
  // concatenated with the inorder traversal of the right subtree
  return inorderTraversal(root.left)
    .concat(root.val)
    .concat(inorderTraversal(root.right));
};

console.log(
  inorderTraversal(
    new TreeNode(
      1,
      new TreeNode(2, new TreeNode(4), new TreeNode(5)),
      new TreeNode(3, new TreeNode(6), new TreeNode(7))
    )
  )
);
