// https://leetcode.com/problems/contains-duplicate

// Given an integer array nums, return true if any value appears at least twice in
// the array, and return false if every element is distinct.

/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function (nums) {
  // unique values in arrays
  let unique_values = Array.from(new Set(nums).values());

  if (unique_values.length != nums.length) {
    return true;
  } else {
    return false;
  }
};

console.log(containsDuplicate([1, 2, 3, 4, 5, 1]));
