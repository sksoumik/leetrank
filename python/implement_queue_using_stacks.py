# https://leetcode.com/problems/implement-queue-using-stacks/ 

# Implement a first in first out (FIFO) queue using only two stacks.
# The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).


class MyQueue:
    def __init__(self):
        # Initialize two stacks for enqueuing and dequeuing
        self.enqueue_stack = []
        self.dequeue_stack = []

    def push(self, x: int) -> None:
        # Push new elements onto the enqueue stack
        self.enqueue_stack.append(x)

    def pop(self) -> int:
        # Transfer elements from the enqueue stack to the dequeue stack
        # if the dequeue stack is empty
        self.transfer_if_necessary()
        # Pop the top element from the dequeue stack
        return self.dequeue_stack.pop()

    def peek(self) -> int:
        # Transfer elements from the enqueue stack to the dequeue stack
        # if the dequeue stack is empty
        self.transfer_if_necessary()
        # Return the top element from the dequeue stack
        return self.dequeue_stack[-1]

    def empty(self) -> bool:
        # Return true if both stacks are empty, false otherwise
        return not self.enqueue_stack and not self.dequeue_stack
    
    def transfer_if_necessary(self) -> None:
        # Transfer all elements from the enqueue stack to the dequeue stack
        # if the dequeue stack is empty
        if not self.dequeue_stack:
            while self.enqueue_stack:
                self.dequeue_stack.append(self.enqueue_stack.pop())



if __name__ == '__main__':
    # Test the solution
    queue = MyQueue()
    queue.push(1)
    queue.push(2)
    print(queue.peek())  # Output: 1
    print(queue.pop())  # Output: 1
    print(queue.pop())  # Output: 2
    print(queue.empty())  # Output: True

