# https://leetcode.com/problems/linked-list-cycle

# Given head, the head of a linked list, determine if the linked list has a cycle in it.

# There is a cycle in a linked list if there is some node in the list that can be
# reached again by continuously following the next pointer. Internally, pos is used
# to denote the index of the node that tail's next pointer is connected to. Note that
# pos is not passed as a parameter.

# Return true if there is a cycle in the linked list. Otherwise, return false.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        """
        Traverse the list one by one and keep putting the node addresses in a Hash Table.
        At any point, if NULL is reached then return false,
        and if the next of the current nodes points to any of the
        previously stored nodes in  Hash then return true.
        """
        # hash table
        hash = set()
        while head:
            # If we already have this node in hashmap it means there is a cycle.
            # because we are at the same node again as we have already visited it once.
            if head in hash:
                return True
            # otherwise add it to hash map
            hash.add(head)

            # move to next node
            head = head.next

        # if we traverse till the end and there is no cycle then return false
        return False


if __name__ == "__main__":
    # Input: 0->1->2->3->4->5->NULL
    # Output: True
    head = ListNode(0)
    head.next = ListNode(1)
    head.next.next = ListNode(2)
    head.next.next.next = ListNode(3)
    head.next.next.next.next = ListNode(4)
    head.next.next.next.next.next = ListNode(5)
    head.next.next.next.next.next.next = head.next.next

    print(Solution().hasCycle(head))
