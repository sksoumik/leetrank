# https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards

# There are several cards arranged in a row, and each card has an associated number of points.
# The points are given in the integer array cardPoints.
# In one step, you can take one card from the beginning or
# from the end of the row. You have to take exactly k cards.
# Your score is the sum of the points of the cards you have taken.
# Given the integer array cardPoints and the integer k, return the maximum score you can obtain.


# Example 1:
# Input: cardPoints = [1,2,3,4,5,6,1], k = 3
# Output: 12
# Explanation: After the first step, your score will always be 1. However,
# choosing the rightmost card first will maximize your total score.
# The optimal strategy is to take the three cards on the right, giving a final score of 1 + 6 + 5 = 12.

from typing import List


class Solution:
    # sliding window
    # time complexity: O(n)
    # space complexity: O(1)
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        cumulative_sum = []
        sums = 0
        for num in cardPoints:
            sums += num
            cumulative_sum.append(sums)

        if k == len(cardPoints):
            return sums

        # subarray that we are going to leave
        subarray_length = len(cardPoints) - k
        window = cumulative_sum[subarray_length - 1]


if __name__ == "__main__":
    cardPoints = [1, 2, 3, 4, 5, 6, 1]
    k = 3
    print(Solution().maxScore(cardPoints, k))  # 12
