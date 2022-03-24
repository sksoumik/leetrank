# https://leetcode.com/problems/excel-sheet-column-number
# Given a string columnTitle that represents the column title as appear in an Excel sheet, 
# return its corresponding column number.

# A -> 1
# B -> 2
# C -> 3
# ...
# Z -> 26
# AA -> 27
# AB -> 28

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        # Convert the column title to a number
        # 1. Convert the first letter to a number
        # 2. Multiply the result by 26
        # 3. Add the second letter to the result
        # 4. Repeat until the last letter
        # 5. Return the result
        result = 0
        for i in range(len(columnTitle)):
            result += (ord(columnTitle[i]) - 64) * 26 ** (len(columnTitle) - i - 1)
        return result

if __name__ == "__main__":
    s = Solution()
    print(s.titleToNumber("A"))
    print(s.titleToNumber("AB"))
    print(s.titleToNumber("ZY"))
    print(s.titleToNumber("AAA"))
    print(s.titleToNumber("ZYX"))

        