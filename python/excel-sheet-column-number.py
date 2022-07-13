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

# video explanation: https://youtu.be/DQKafgIBeyI

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        multiplier = 1
        column = 0
        # A for loop that starts at the end of the string and goes backwards by 1 character
        for i in range(len(columnTitle) - 1, -1, -1):
            column += (ord(columnTitle[i]) - 64) * multiplier
            multiplier *= 26
        return column

if __name__ == "__main__":
    s = Solution()
    print(s.titleToNumber("A"))
    print(s.titleToNumber("AB"))
    print(s.titleToNumber("ZY"))
    print(s.titleToNumber("AAA"))
    print(s.titleToNumber("ZYX"))

        