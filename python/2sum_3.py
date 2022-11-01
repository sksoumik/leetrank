# leetcode premium problem
# https://leetcode.com/problems/two-sum-iii-data-structure-design/

# Design and implement a TwoSum class. It should support the following operations: add and find.

# add - Add the number to an internal data structure.
# find - Find if there exists any pair of numbers which sum is equal to the value.

# Example 1:

# add(1); add(3); add(5);
# find(4) -> true
# find(7) -> false

import collections


class TwoSum:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums_map = collections.defaultdict(int)

    def add(self, number: int) -> None:
        """
        Add the number to an internal data structure..
        """
        self.nums_map[number] += 1

    def find(self, value: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """
        for num in self.nums_map:
            target = value - num
            if target in self.nums_map and (target != num or self.nums_map[target] > 1):
                return True
        return False


if __name__ == "__main__":
    twoSum = TwoSum()
    twoSum.add(1)
    twoSum.add(3)
    twoSum.add(5)
    print(twoSum.find(4))  # True
    print(twoSum.find(7))  # False
