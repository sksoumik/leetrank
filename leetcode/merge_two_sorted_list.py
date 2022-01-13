# https://leetcode.com/problems/merge-two-sorted-lists/
# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists in a one sorted list. The list should be
# made by splicing together the nodes of the first two lists.


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


# singly LinkedList
class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def print_list(self):
        curr = self.head
        while curr:
            print(curr.val, end=" ")
            curr = curr.next
        print()

    # append item at the beginning of the list
    def push_start(self, val):
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node
    


if __name__ == "__main__":
    list1 = LinkedList(Node(1))
    list1.head.next = Node(3)
    list1.head.next.next = Node(5)
    list1.head.next.next.next = Node(7)

    list2 = LinkedList(Node(2))
    list2.head.next = Node(4)
    list2.head.next.next = Node(6)
    list2.head.next.next.next = Node(8)

    list1.print_list()
    list2.print_list()

    # add item at the beginning of the list
    list1.push_start(10)
    list1.print_list()

