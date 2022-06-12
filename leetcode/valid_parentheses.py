# https://leetcode.com/problems/valid-parentheses

# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.

# video explanation: https://youtu.be/WTzjTskDFMg


class Solution:
    def isValid(self, s: str) -> bool:
        # map all closed brackets to their opening brackets
        # we will search for the opening bracket of the closed bracket
        # if we find it, we will remove it from the stack
        # if we don't find it, we will return false
        map = {")": "(", "]": "[", "}": "{"}
        stack = []
        # This is checking if the current character is a closing bracket. If it is, we check if the
        # stack is empty or if the last element in the stack is not the opening bracket of the current
        # closing bracket. If either of these are true, we return false.
        for char in s:
            if char in map:
                if not stack or stack.pop() != map[char]:

                    return False
            else:
                stack.append(char)

        return True if not stack else False


if __name__ == "__main__":
    sol = Solution()
    print(sol.isValid("()"))
    print(sol.isValid("()[]{}"))
    print(sol.isValid("(]"))
    print(sol.isValid("([)]"))
    print(sol.isValid("{[]}"))
