# https://leetcode.com/problems/middle-of-the-linked-list

# Given the head of a singly linked list, return the middle node of the linked list.
# If there are two middle nodes, return the second middle node.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head):
        """
        return the middle node and afterwards of the linked list
        :type head: ListNode
        :rtype: ListNode
        """
        # Initialize two pointers, one will go one step a time (slow),
        # another pointer two steps a time (fast).
        slow = head
        fast = head
        # Iterate till fast's next is null (fast reaches to the end).
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # return slow.val
        # return the slow's data, which would be the middle element.
        return slow


if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    head.next.next.next.next.next = ListNode(6)

    print(Solution().middleNode(head))
