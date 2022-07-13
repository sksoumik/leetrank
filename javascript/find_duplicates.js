// find dupliate elements in an array
// Solution: O(n), because it only iterates the list once and set lookups are O(1)

var findDuplicate = function (nums) {
  let set = new Set();
  let duplicate = [];

  for (let i = 0; i < nums.length; i++) {
    if (set.has(nums[i])) {
      duplicate.push(nums[i]);
    } else {
      set.add(nums[i]);
    }
  }
  return duplicate;
};

console.log(findDuplicate([1, 2, 3, 1, 3]));
