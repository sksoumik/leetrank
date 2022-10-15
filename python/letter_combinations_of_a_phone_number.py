# https://leetcode.com/problems/letter-combinations-of-a-phone-number

# Given a string containing digits from 2-9 inclusive,
# return all possible letter combinations that the number could represent.
# Return the answer in any order.

# A mapping of digits to letters (just like on the telephone buttons) is given below.
# Note that 1 does not map to any letters.


# Example 1:
# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        phone_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        output = []

        def backtrack(i, current_str):
            # base case
            if len(current_str) == len(digits):
                output.append(current_str)
                return

            for c in phone_map[digits[i]]:
                backtrack(i + 1, current_str + c)

        if digits:
            backtrack(0, "")

        return output


if __name__ == "__main__":
    solution = Solution()
    print(solution.letterCombinations("23"))
