# https://leetcode.com/problems/roman-to-integer/

# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000

# vid: https://youtu.be/3jdxYj3DD98


class Solution:
    # time complexity: O(n)
    # space complexity: O(1)
    def romanToInt(self, s: str) -> int:
        roman_map = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        result = 0

        for i in range(len(s)):
            # check inbounds and if the previous value is less than the current value
            # then previous value would be subtracted from the result
            if i + 1 < len(s) and roman_map[s[i]] < roman_map[s[i + 1]]:
                result -= roman_map[s[i]]
            else:
                result += roman_map[s[i]]

        return result


if __name__ == "__main__":
    solution = Solution()
    print(solution.romanToInt("III"))
    print(solution.romanToInt("IV"))
    print(solution.romanToInt("IX"))
    print(solution.romanToInt("LVIII"))
    print(solution.romanToInt("MCMXCIV"))
