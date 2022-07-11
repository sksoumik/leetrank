// https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/646/

/**
 * @param {number[]} nums
 * @param {number} k
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var rotate = function (nums, k) {
    if (k == 0) {
        return;
    }
    k = k % nums.length;
    m = nums.length - k;
    // inplace swap
    for (let i = 0; i < m; i++) {
        let temp = nums[i];
        nums[i] = nums[i + k];
        nums[i + k] = temp;
    }

    console.log(nums);

};

console.log(rotate([1, 2, 3, 4, 5, 6, 7], 3));
console.log(rotate([1, 2], 3));
