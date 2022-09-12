# https://leetcode.com/problems/min-cost-climbing-stairs

# You are given an integer array cost where cost[i] is the cost of ith step on a staircase.
# Once you pay the cost, you can either climb one or two steps.
# You can either start from the step with index 0, or the step with index 1.
# Return the minimum cost to reach the top of the floor.


# Example 1:

# Input: cost = [10,15,20]
# Output: 15
# Explanation: You will start at index 1.
# - Pay 15 and climb two steps to reach the top.
# The total cost is 15.

# video explanation: https://youtu.be/uJmMJcxbozw
from typing import List


class Solution:
    # time complexity: O(n), space complexity: O(1)
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # [1,100, 1, 1, 1, 100, 1, 1, 100, 1]
        # start calculating from index 2, because we need 2 previous steps to calculate the current step
        # [1,100, 2, 3, 3, 103, 4, 5, 104, 6]

        for step in range(2, len(cost)):
            cost[step] += min(cost[step - 1], cost[step - 2])
        # return the minimum between the last two steps
        return min(cost[-1], cost[-2])


if __name__ == "__main__":
    s = Solution()

    cost = [10, 15, 20]
    print(s.minCostClimbingStairs(cost))

    cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    print(s.minCostClimbingStairs(cost))
