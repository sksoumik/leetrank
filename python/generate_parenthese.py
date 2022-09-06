# https://leetcode.com/problems/generate-parentheses/

# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

# Example 1:

# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
# Example 2:

# Input: n = 1
# Output: ["()"]

from typing import List


class Solution:
    # video explanation: https://youtu.be/s9fokUqJ76A

    # time complexity O(2^n)
    def generateParenthesis(self, n: int) -> List[str]:
        # a stack where the parenthesis are pushed and popped
        stack = []
        result = []

        def backtrack(open_count, close_count):
            # valid only if open_count == close_count == n
            # base case
            if open_count == close_count == n:
                result.append("".join(stack))
                return

            # if open_count < n, push a open parenthesis
            if open_count < n:
                stack.append("(")
                backtrack(open_count + 1, close_count)
                # clear the stack
                stack.pop()

            # if close_count < open_count, push a close parenthesis
            # we can only push a close parenthesis, if close_count < open_count
            if close_count < open_count:
                stack.append(")")
                backtrack(open_count, close_count + 1)
                # clear the stack
                stack.pop()

        backtrack(0, 0)
        return result

if __name__ == "__main__":
    s = Solution()
    print(s.generateParenthesis(3))
