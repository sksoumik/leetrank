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

# naive implementation
class TwoSum:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums = []

    def add(self, number: int) -> None:
        """
        Add the number to an internal data structure..
        """
        self.nums.append(number)

    def find(self, value: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """
        for i in range(len(self.nums)):
            for j in range(i + 1, len(self.nums)):
                if self.nums[i] + self.nums[j] == value:
                    return True
        return False


# optimized implementation using hash table
class TwoSum2:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums_map = []

    def add(self, number: int) -> None:
        """
        Add the number to an internal data structure..
        """
        self.nums_map.append(number)

    def find(self, value: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """
        hash_table = {}

        for num in self.nums_map:
            if value - num in hash_table:
                return True
            hash_table[num] = True

        return False


# optimized implementation using hash table
class TwoSum3:
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
            if target in self.nums_map and (target != num or self.nums_map[num] > 1):
                return True
        return False


if __name__ == "__main__":
    twoSum = TwoSum2()
    twoSum.add(1)
    twoSum.add(3)
    twoSum.add(5)
    print(twoSum.find(4))  # True
    print(twoSum.find(7))  # False

    twoSum = TwoSum3()
    twoSum.add(1)
    twoSum.add(3)
    twoSum.add(5)
    print(twoSum.find(4))  # True
    print(twoSum.find(7))  # False
