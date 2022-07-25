# https://leetcode.com/problems/remove-duplicates-from-sorted-list/

# Given the head of a sorted linked list, delete all duplicates such that each element appears only once. 
# Return the linked list sorted as well.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head):
        """
        If the current node's value is the same as the next node's value, then skip the next node
        because it is a sorted linked list.
        
        :param head: the head of the linked list
        :return: The head of the linked list.
        """
        if not head:
            return None
        
        if not head.next:
            return head
    
        current_node = head
        while current_node.next:
            if current_node.val == current_node.next.val:
                current_node.next = current_node.next.next
            else:
                current_node = current_node.next    

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
    current_node = head
    while current_node:
        print(current_node.val)
        current_node = current_node.next
    # delete the duplicates
    head = Solution().deleteDuplicates(head)
    # print the linked list after deleting the duplicates
    print("After deleting the duplicates:")
    current_node = head
    while current_node:
        print(current_node.val)
        current_node = current_node.next

    