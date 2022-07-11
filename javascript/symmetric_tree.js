// https://leetcode.com/problems/symmetric-tree

// Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {boolean}
 */

function TreeNode(val, left, right) {
    this.val = (val === undefined ? 0 : val);
    this.left = (left === undefined ? null : left);
    this.right = (right === undefined ? null : right);
}


var isSymmetric = function (root) {
    if (!root) {
        return true;
    }
    return isMirror(root.left, root.right);
};

var isMirror = function (left, right) {
    if (!left && !right) {
        return true;
    }
    if (!left || !right) {
        return false;
    }
    return left.val === right.val &&
        isMirror(left.left, right.right) &&
        isMirror(left.right, right.left);
}


var root = new TreeNode(1, new TreeNode(2, new TreeNode(3), new TreeNode(4)), new TreeNode(2, new TreeNode(4), new TreeNode(3)));
console.log(isSymmetric(root));



