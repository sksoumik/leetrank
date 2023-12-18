# https://leetcode.com/problems/min-stack/description/

# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

# Implement the MinStack class:

# MinStack() initializes the stack object.
# void push(int val) pushes the element val onto the stack.
# void pop() removes the element on the top of the stack.
# int top() gets the top element of the stack.
# int getMin() retrieves the minimum element in the stack.
# You must implement a solution with O(1) time complexity for each function.


class MinStack:
    def __init__(self):
        # initialize two stacks; one for storing elements and another
        # one for tracking the minimum element
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        # Update min_stack only if the current value is smaller or equal to the current minimum
        # check if the min_stack is empty or if the current value is smaller or equal to the current minimum
        if not self.min_stack or val <= self.min_stack[-1]:
            # if so, append the current value to the min_stack
            self.min_stack.append(val)

    def pop(self) -> None:
        # check if the stack is empty before popping
        if self.stack:
            # if the top element of the stack is equal to the top element of the min_stack
            if self.stack[-1] == self.min_stack[-1]:
                # pop the top element of the min_stack
                self.min_stack.pop()
            # always pop the top element from the main stack
            self.stack.pop()

    def top(self) -> int:
        # check if the stack is empty before returning the top element
        if self.stack:
            # return the top element of the stack
            return self.stack[-1]
        # if the stack is empty, return -1
        return -1

    def getMin(self) -> int:
        if self.min_stack:
            # return the top element of the min_stack
            return self.min_stack[-1]


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(3)
obj.push(2)
obj.push(1)
obj.pop()
param_3 = obj.top()
param_4 = obj.getMin()
print(param_3)
print(param_4)
