# https://leetcode.com/problems/length-of-last-word/
# Given a string s consisting of some words separated by some number of spaces, r
# eturn the length of the last word in the string.
# A word is a maximal substring consisting of non-space characters only.


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        """
        We strip the string of whitespace, split it into a list of words, and return the length of the
        last word

        :param s: str
        :type s: str
        :return: The length of the last word in the string.
        """
        if s == "":
            return 0
        s = s.strip()
        splitted = s.split(" ")
        last_word = splitted[-1]
        return len(last_word)


if __name__ == "__main__":
    s = Solution()
    print(s.lengthOfLastWord("Hello World"))
    print(s.lengthOfLastWord("Hello"))
    print(s.lengthOfLastWord(""))
    print(s.lengthOfLastWord("  fly me   to   the moon  "))
