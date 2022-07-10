# https://leetcode.com/problems/reverse-linked-list

# Given the head of a singly linked list, reverse the list, and return the reversed list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head):
        """
        Method 1: Iterative way
        We are reversing the direction of the pointers of the nodes in the linked list.
        
        :param head: the head of the linked list
        :return: The reversed linked list.
        """

        prev = None
        curr = head
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev

    def reverseList_2(self, head):
        """
        Method 2: Recursive way
        We are reversing the direction of the pointers of the nodes in the linked list. 
        We are also reversing the order of the nodes in the linked list.

        :param head: the head of the linked list
        :return: The reversed linked list.
        """
        # This is a base case for the recursive function.
        if not head or not head.next:
            return head
        # Recursively calling the function on the next node in the linked list.
        new_head = self.reverseList_2(head.next)
        # Reversing the direction of the pointers of the nodes in the linked list.
        head.next.next = head
        # Setting the next pointer of the last node in the linked list to None.
        head.next = None
        return new_head

    
    # print the linked list
    def print_list(self, head):
        """
        Prints the values of the linked list.
        
        :param head: the head of the linked list
        """
        while head:
            print(head.val, end=" ")
            head = head.next

if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)

    sol = Solution()
    sol.print_list(head)
    print("\n")
    sol.print_list(sol.reverseList(head))


        