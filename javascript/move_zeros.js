// https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/567/
// Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
// Note that you must do this in-place without making a copy of the array.

// Example 1:
// Input: nums = [0,1,0,3,12]
// Output: [1,3,12,0,0]

/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var moveZeroes = function (nums) {
    let j = 0;

    for (let i = 0; i < nums.length; i++) {
        if (nums[i] !== 0) {
            // swap nums[j] with nums[i]
            let temp = nums[j];
            nums[j] = nums[i];
            nums[i] = temp;
            j++;
        }
    }
};

// console.log(moveZeroes([0,1,0,3,12]));


