// https://leetcode.com/problems/find-the-duplicate-number
//
// Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
//
// There is only one repeated number in nums, return this repeated number.
//
// You must solve the problem without modifying the array nums and uses only constant extra space.

var findDuplicate = function (nums) {
  let seen = new Set();

  for (let i = 0; i < nums.length; i++) {
    if (seen.has(nums[i])) {
      return nums[i];
    } else {
      seen.add(nums[i]);
    }
  }

  return -1;
};

console.log(findDuplicate([1, 2, 3, 1, 3]));
