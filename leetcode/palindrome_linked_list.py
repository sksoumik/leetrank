# https://leetcode.com/problems/palindrome-linked-list
# Given the head of a singly linked list, return true if it is a palindrome.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head) -> bool:
        """
        :type head: ListNode
        :rtype: bool

        A simple solution is to use a stack of list nodes. This mainly involves three steps.

        1. Traverse the given list from head to tail and push every visited node to stack.
        2. Traverse the list again. For every visited node, pop a node from the stack and
           compare data of popped node with the currently visited node.
        3. If all nodes matched, then return true, else false.

        Note: Stack follows LIFO (Last In First Out) order. e.g. Stacking Plates
        pop(): Accessing the content while removing it from the stack, is known as a Pop Operation.
               delete the last item.

        """
        # if list is empty
        if not head:
            return True
        # if list has only one node
        if not head.next:
            return True
        # if list has more than one node
        # create a stack
        stack = []
        # create a pointer
        pointer = head
        # while pointer is not None
        while pointer:
            # push the value of the node to the stack
            stack.append(pointer.val)
            # move the pointer to the next node
            pointer = pointer.next

        # create a pointer again
        pointer = head
        # while pointer is not None
        while pointer:
            # check if the value of the node is the same as the top of the stack
            if pointer.val != stack.pop():
                return False
            # move the pointer to the next node
            pointer = pointer.next
        # return true if the list is a palindrome
        return True


if __name__ == "__main__":
    # create a linked list
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(2)
    head.next.next.next = ListNode(1)
    # create a solution
    solution = Solution()
    # check if the list is a palindrome
    print(solution.isPalindrome(head))
    # create a linked list
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(2)
    head.next.next.next.next = ListNode(1)
    # check if the list is a palindrome
    print(solution.isPalindrome(head))
