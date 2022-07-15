// https://leetcode.com/problems/first-unique-character-in-a-string

// Given a string s, find the first non-repeating character in it and return its index.
// If it does not exist, return -1.

// Example 1:

// Input: s = "leetcode"
// Output: 0

var firstUniqChar = function (s) {
  // if the s is empty, return -1
  if (s.length === 0) return -1;

  // create a hash table to store the characters and their counts
  let hash = {};

  // iterate through the string
  for (let i = 0; i < s.length; i++) {
    // if the character is not in the hash table, add it and set its count to 1
    if (!hash[s[i]]) {
      hash[s[i]] = 1;
    } else {
      // if the character is in the hash table, increment its count
      hash[s[i]]++;
    }
  }

  // iterate through the string again
  for (let i = 0; i < s.length; i++) {
    // if the character's count is 1, return its index
    if (hash[s[i]] === 1) {
      return i;
    }
  }

  // if no unique character is found, return -1
  return -1;
};

console.log(firstUniqChar("leetcode"));
