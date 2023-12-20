# https://leetcode.com/problems/evaluate-reverse-polish-notation/description/

# You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

# Evaluate the expression. Return an integer that represents the value of the expression.

# Note that:

# The valid operators are '+', '-', '*', and '/'.
# Each operand may be an integer or another expression.
# The division between two integers always truncates toward zero.
# There will not be any division by zero.
# The input represents a valid arithmetic expression in a reverse polish notation.
# The answer and all the intermediate calculations can be represented in a 32-bit integer.

from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == "+":
                stack.append(stack.pop() + stack.pop())
            elif token == "-":
                stack.append(-stack.pop() + stack.pop())
            elif token == "*":
                stack.append(stack.pop() * stack.pop())
            elif token == "/":
                stack.append(int(1 / stack.pop() * stack.pop()))
            else:
                stack.append(int(token))
        return stack[0]


# driver code
s = Solution()
tokens = ["2", "1", "+", "3", "*"]
print(s.evalRPN(tokens))
tokens = ["4", "13", "5", "/", "+"]
print(s.evalRPN(tokens))
