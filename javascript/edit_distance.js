// https://leetcode.com/problems/edit_distance

// Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

// You have the following three operations permitted on a word:

// Insert a character
// Delete a character
// Replace a character

// Example 1:
// Input: word1 = "horse", word2 = "ros"
// Output: 3
// Explanation:
// horse -> rorse (replace 'h' with 'r')
// rorse -> rose (remove 'r')
// rose -> ros (remove 'e')

var minDistance = function (word1, word2) {
  // if word1 is empty, then we have to insert all characters of word2
  if (word1.length === 0) return word2.length;
  // if word2 is empty, then we have to delete all characters of word1
  if (word2.length === 0) return word1.length;
  // if the two strings are the same
  if (word1[0] === word2[0]) {
    return minDistance(word1.slice(1), word2.slice(1));
  }
  // if the two strings are not the same
  // we have to find the minimum of the three operations
  return (
    1 +
    Math.min(
      minDistance(word1.slice(1), word2.slice(1)), // diagonal
      minDistance(word1.slice(1), word2), // previous row
      minDistance(word1, word2.slice(1)) // previous column
    )
  );
};
