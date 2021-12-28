# https://leetcode.com/problems/middle-of-the-linked-list/
# Given the head of a singly linked list, return the middle node of the linked list.
# If there are two middle nodes, return the second middle node.


class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


class Solution:
    def push(self, node, value):
        new_node = LinkedList(value)
        new_node.next = node
        return new_node

    def middleNode(self, head: LinkedList) -> LinkedList:
        # method 1: O (n) solution: hash table
        # We can start with brute-force approach. To return the middle node, we need to know the length of
        # the linked-list. So, we perform the 1st iteration from start to end of linked list and count
        # the number of nodes N. Then, in the next loop, we iterate till N/2th, i.e, the middle node and return it
        iterate, count = head, 0
        while iterate:
            iterate = iterate.next
            count += 1
        for i in range(count // 2):
            head = head.next
        return head

    # print the items in the linked list
    def print_linked_list(self, head):
        while head:
            print(head.value, end=" ")
            head = head.next
        print()

    def push(self, node, value):
        new_node = LinkedList(value)
        new_node.next = node
        return new_node


if __name__ == "__main__":
    # test case 1
    head = LinkedList(1)
    head = Solution().push(head, 2)
    head = Solution().push(head, 3)
    head = Solution().push(head, 4)
    head = Solution().push(head, 5)
    Solution().print_linked_list(head)
    print(Solution().middleNode(head).value)

    # test case 2
    head = LinkedList(1)
    head = Solution().push(head, 2)
    head = Solution().push(head, 3)
    head = Solution().push(head, 4)
    Solution().print_linked_list(head)
    print(Solution().middleNode(head).value)

    # test case 3
    head = LinkedList(1)
    head = Solution().push(head, 2)
    head = Solution().push(head, 3)
    Solution().print_linked_list(head)
    print(Solution().middleNode(head).value)
