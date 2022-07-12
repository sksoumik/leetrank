// https://leetcode.com/problems/container-with-most-water
// You are given an integer array height of length n. There are n vertical
// lines drawn such that the two endpoints of the ith line are (i, 0)
// and (i, height[i]).
// Find two lines that together with the x-axis form a container, such
// that the container contains the most water.
// Return the maximum amount of water a container can store.
// Notice that you may not slant the container.

// video explanation: https://youtu.be/Uj3gJjg6SXc

/**
 * @param {number[]} height
 * @return {number}
 */
var maxArea = function (height) {
  let max_area = 0;
  let left = 0;
  let right = height.length - 1;
  while (left < right) {
    let area = Math.min(height[left], height[right]) * (right - left);
    max_area = Math.max(max_area, area);
    if (height[left] < height[right]) {
      left++;
    } else {
      right--;
    }
  }
  return max_area;
};
