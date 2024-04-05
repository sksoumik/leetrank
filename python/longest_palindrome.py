# https://leetcode.com/problems/longest-palindrome/

# Given a string s which consists of lowercase or uppercase letters,
# return the length of the longest palindrome that can be built with those letters.
# Letters are case sensitive, for example, "Aa" is not considered a palindrome here.


# Example 1:

# Input: s = "abccccdd"
# Output: 7
# Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.


from collections import Counter


class Solution:
    # without using any external library
    def longestPalindrome_1(self, s: str) -> int:
        """
        We count the number of characters in the string, and if there are any odd counts, we subtract the
        number of odd counts from the length of the string, and add 1 to the result.

        If there are no odd counts, we return the length of the string.

        The reason we add 1 to the result is because we can always have a palindrome of odd length by using
        the character with the odd count as the center of the palindrome.

        For example, if we have the string "aabbcc", we can have a palindrome of length 5 by using the
        character 'b' as the center of the palindrome.

        If we have the string "aabbccc", we can have a palindrome of length 7 by using the character 'c' as
        the center of the palindrome.


        :param s: the string we're checking
        :type s: str
        :return: The length of the longest palindrome that can be built from the input string.
        """
        char_count = {}

        for c in s:
            if c in char_count:
                char_count[c] += 1
            else:
                char_count[c] = 1

        odd_count = 0
        for c in char_count:
            if char_count[c] % 2 == 1:
                odd_count += 1

        return len(s) - odd_count + 1 if odd_count > 0 else len(s)

    # using Counter from collections
    def longestPalindrome(self, s: str) -> int:
        c = Counter(s)
        odd_count = 0
        for k, v in c.items():
            if v % 2 == 1:
                odd_count += 1
        return len(s) - odd_count + 1 if odd_count > 0 else len(s)


if __name__ == "__main__":
    s = "abccccdd"
    print(Solution().longestPalindrome(s))
