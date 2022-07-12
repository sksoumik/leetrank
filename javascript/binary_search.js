// https://leetcode.com/problems/binary-search/

// Given an array of integers nums which is sorted in ascending order,
// and an integer target, write a function to search target in nums.
// If target exists, then return its index. Otherwise, return -1.
// You must write an algorithm with O(log n) runtime complexity.

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var search = function (nums, target) {
  let i = 0;
  let j = nums.length - 1;
  while (i <= j) {
    let idx_of_mid = Math.floor((i + j) / 2);
    let mid_element = nums[idx_of_mid];
    if (target === mid_element) {
      return idx_of_mid;
    }
    if (target > mid_element) {
      i = idx_of_mid + 1;
    } else {
      j = idx_of_mid - 1;
    }
  }
  return -1;
};

console.log(search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5));
