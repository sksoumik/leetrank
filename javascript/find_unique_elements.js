// unique elements and appeared only once is not the same.
// unique is means, occurrence of the same element is 1.

// For example,

// nums = [1, 2, 3, 2, 3]
// unique elements (set) will return `[1, 2, 3]` but
// appeared only once will return `[1]`.

var get_unique = function (nums) {
  // count the number of occurrences of each element
  let count = {};
  for (let i = 0; i < nums.length; i++) {
    if (count[nums[i]]) {
      count[nums[i]]++;
    } else {
      count[nums[i]] = 1;
    }
  }

  // find the element that occurs only once in count
  let appeared_once = [];
  for (let key in count) {
    if (count[key] === 1) {
      // push the number in integer formate to the array
      appeared_once.push(parseInt(key));
    }
  }

  return appeared_once;
};

console.log(get_unique([1, 2, 3, 2, 3, 8, 11]));
