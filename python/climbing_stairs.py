# https://leetcode.com/problems/climbing-stairs

# You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps. In how many distinct
# ways can you climb to the top?

# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps

# recursive solution
# will cause runtime error
class SolutionRecursive:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)


# dynamic programming
class Solution:
    def climbStairs(self, n: int) -> int:
        """
        We're building a table of the number of ways to climb to each step, starting with the base cases
        of 0, 1, and 2
        
        :param n: the number of steps we want to climb
        :type n: int
        :return: The number of ways to climb the stairs.
        """
        table = [0, 1, 2]

        for i in range(3, n + 1):
            table.append(table[i - 1] + table[i - 2])
        return table[n]


if __name__ == "__main__":
    s = Solution()
    print(s.climbStairs(2))
    print(s.climbStairs(3))
    print(s.climbStairs(4))
    print(s.climbStairs(5))

