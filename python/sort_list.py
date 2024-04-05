# https://leetcode.com/problems/sort-list/

# Given the head of a linked list, return the list after sorting it in ascending order.

# Input: head = [4,2,1,3]
# Output: [1,2,3,4]


from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution2:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Convert linked list to a list
        vals = []
        current = head
        while current:
            vals.append(current.val)
            current = current.next

        # Sort the list
        vals.sort()

        # Convert the list back to a linked list
        current = head
        for val in vals:
            current.val = val
            current = current.next
        return head


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        # find the middle node
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # cut the list into two halves
        mid = slow.next
        slow.next = None

        # sort each half
        left = self.sortList(head)
        right = self.sortList(mid)

        # merge the two sorted lists
        return self.merge(left, right)

    def merge(self, left, right):
        dummy = ListNode()
        tail = dummy

        while left and right:
            if left.val < right.val:
                tail.next = left
                left = left.next
            else:
                tail.next = right
                right = right.next
            tail = tail.next

        if left:
            tail.next = left
        if right:
            tail.next = right

        return dummy.next


if __name__ == "__main__":
    # Input: head = [4,2,1,3]
    # Output: [1,2,3,4]
    head = ListNode(4)
    head.next = ListNode(2)
    head.next.next = ListNode(1)
    head.next.next.next = ListNode(3)

    print(Solution().sortList(head))
