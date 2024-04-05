# https://leetcode.com/problems/richest-customer-wealth

# You are given an m x n integer grid accounts where accounts[i][j] is
# the amount of money the i​​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank.
# Return the wealth that the richest customer has.

# A customer's wealth is the amount of money they have in all their bank accounts.
# The richest customer is the customer that has the maximum wealth.


# Example 1:

# Input: accounts = [[1,2,3],[3,2,1]]
# Output: 6

from typing import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max(sum(account) for account in accounts)


if __name__ == "__main__":
    sol = Solution()
    accounts = [[1, 2, 3], [3, 2, 1]]
    print(sol.maximumWealth(accounts))
    accounts = [[1, 5], [7, 3], [4, 2]]
    print(sol.maximumWealth(accounts))
    accounts = [[2, 8, 4], [1, 5, 7, 9], [1, 7, 8, 4, 2]]
    print(sol.maximumWealth(accounts))
