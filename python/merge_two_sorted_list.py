# https://leetcode.com/problems/merge-two-sorted-lists/
# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists in a one sorted list. The list should be
# made by splicing together the nodes of the first two lists.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1, list2):
        # if any of the lists are empty,
        if not list1 or not list2:
            # return the other list
            return list1 or list2

        # if list1 is less than list2
        if list1.val < list2.val:
            # set the next node to the next node of list1
            list1.next = self.mergeTwoLists(list1.next, list2)
            # return list1
            return list1
        else:
            # set the next node to the next node of list2
            list2.next = self.mergeTwoLists(list1, list2.next)
            # return list2
            return list2

    # print the linkedList
    def printList(self, node):
        while node:
            print(node.val, end=" ")
            node = node.next
        print()


if __name__ == "__main__":
    # create a list
    list1 = ListNode(1)
    list1.next = ListNode(2)
    list1.next.next = ListNode(4)

    # create a list
    list2 = ListNode(1)
    list2.next = ListNode(3)
    list2.next.next = ListNode(4)

    # create a solution object
    solution = Solution()

    # merge the two lists
    merged_list = solution.mergeTwoLists(list1, list2)

    # print the merged list
    solution.printList(merged_list)
