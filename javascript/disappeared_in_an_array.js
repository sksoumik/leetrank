// https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

// Given an array nums of n integers where nums[i] is in the range [1, n],
// return an array of all the integers in the range [1, n] that do not appear in nums.
// Example 1
// Input: nums = [4,3,2,7,8,2,3,1]
// Output: [5,6]

var findDisappearedNumbers = function (nums) {
  // declare an empty array
  let all_nums = [];

  // iterate through the array
  for (let i = 1; i <= nums.length; i++) {
    // add all the numbers to the all_nums
    all_nums.push(i);
  }

  //find all uncommon numbers between the all_nums and nums
  let uncommon_nums = all_nums.filter((num) => !nums.includes(num));
  return uncommon_nums;
};

console.log(findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]));
