# https://leetcode.com/problems/two-sum-iii-data-structure-design/
# leetcode premium problem

# Design a data structure that accepts a stream of integers
# and checks if it has a pair of integers that sum to a given value.
# Implement the TwoSum class:
# TwoSum() Initializes the object with no pairs
# add - Add the number to an internal data structure.
# find - Find if there exists any pair of numbers which sum is equal to the value.

# Example 1:

# add(1); add(3); add(5);
# find(4) -> true
# find(7) -> false


class TwoSum:
    def __init__(self):
        # initialize your data structure here
        self.output = []

    def add(self, number: int) -> None:
        self.output.append(number)

    def find(self, value: int) -> bool:
        # consider the value as the target
        hash_table = {}
        for idx, num in enumerate(self.output):
            complement = value - num
            if complement in hash_table:
                return True
            hash_table[num] = idx
        return False


if __name__ == "__main__":
    obj = TwoSum()
    obj.add(1)
    obj.add(3)
    obj.add(5)
    print(obj.find(4))
    print(obj.find(7))
