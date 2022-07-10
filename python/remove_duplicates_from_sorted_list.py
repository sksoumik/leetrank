# https://leetcode.com/problems/remove-duplicates-from-sorted-list/

# Given the head of a sorted linked list, delete all duplicates such that each element appears only once. 
# Return the linked list sorted as well.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # method 1
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # if list is empty
        if not head:
            return None
        # if list has only one node
        if not head.next:
            return head
        # if list has more than one node
        # create a pointer
        pointer = head
        # while pointer is not None
        while pointer:
            # create a pointer2
            pointer2 = pointer
            # while pointer2 is not None
            while pointer2.next:
                # if the value of the node is the same as the value of the next node
                if pointer.val == pointer2.next.val:
                    # delete the next node
                    pointer2.next = pointer2.next.next
                # else move the pointer2 to the next node
                else:
                    pointer2 = pointer2.next
            # move the pointer to the next node
            pointer = pointer.next
        # return the head of the list
        return head



if __name__ == "__main__":
    # create a linked list
    head = ListNode(1)
    head.next = ListNode(1)
    head.next.next = ListNode(2)
    head.next.next.next = ListNode(3)
    head.next.next.next.next = ListNode(3)
    # print the linked list
    print("The linked list is:")
    pointer = head
    while pointer:
        print(pointer.val)
        pointer = pointer.next
    # delete the duplicates
    head = Solution().deleteDuplicates(head)
    # print the linked list after deleting the duplicates
    print("After deleting the duplicates:")
    pointer = head
    while pointer:
        print(pointer.val)
        pointer = pointer.next

    