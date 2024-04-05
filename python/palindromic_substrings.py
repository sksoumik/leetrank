# https://leetcode.com/problems/palindromic-substrings/description/

# Given a string s, return the number of palindromic substrings in it.
# A string is a palindrome when it reads the same backward as forward.
# A substring is a contiguous sequence of characters within the string.


# Example 1:

# Input: s = "abc"
# Output: 3
# Explanation: Three palindromic strings: "a", "b", "c".
# Example 2:

# Input: s = "aaa"
# Output: 6
# Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".


class Solution:
    def countSubstrings(self, s: str) -> int:
        # Initialize a counter to keep track of the number of palindromes found
        palindrome_count = 0

        # Iterate through each character in the input string
        for i in range(len(s)):
            # Check for palindromes with odd length (e.g. "aba")
            palindrome_count += self.expandFromCenter(s, i, i)
            # Check for palindromes with even length (e.g. "abba")
            palindrome_count += self.expandFromCenter(s, i, i + 1)

        # Return the total number of palindromic substrings
        return palindrome_count

    def expandFromCenter(self, s, left, right):
        # Initialize a counter to keep track of the number of palindromes
        # found while expanding from the center
        count = 0

        # While the indices are within the bounds of the string
        # and the characters at these indices are equal,
        # increment the counter and move the indices outward
        while left >= 0 and right < len(s) and s[left] == s[right]:
            count += 1
            left -= 1
            right += 1

        # Return the number of palindromes found
        return count


if __name__ == "__main__":
    # Test the solution
    s = "abc"
    print(Solution().countSubstrings(s))  # Output: 3

    s = "aaa"
    print(Solution().countSubstrings(s))  # Output: 6

    s = "aaaaa"
    print(Solution().countSubstrings(s))  # Output: 15
