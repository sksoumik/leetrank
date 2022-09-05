# https://leetcode.com/problems/reverse-linked-list

# Given the head of a singly linked list, reverse the list, and return the reversed list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # time complexity: O(n), space complexity: O(1)
    # space is O(1), because we are only using two pointers, no extra data structure
    # iterative solution
    def reverseListIter(self, head):
        # iterate and swap
        previous, current = None, head  # we will store reversed list in previous
        while current:
            current.next, previous, current = previous, current, current.next

        return previous

    # recursive solution
    # time complexity: O(n), space complexity: O(1)
    def reverseListRec(self, head):
        # base case
        if head is None or head.next is None:
            return head

        node, head.next.next, head.next = self.reverseListRec(head.next), head, None
        return node

    def print_list(self, head):
        while head:
            print(head.val, end=" ")
            head = head.next


if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)

    sol = Solution()
    sol.print_list(head)  # 1 2 3 4
    print()
    sol.print_list(sol.reverseListIter(head))  # 4 3 2 1
    print()

    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)

    sol.print_list(sol.reverseListRec(head))  # 4 3 2 1
