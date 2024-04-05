# https://leetcode.com/problems/top-k-frequent-elements

# Given an integer array nums and an integer k,
# return the k most frequent elements. You may return the answer in any order.


# Example 1:
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]

# Example 2:
# Input: nums = [1], k = 1
# Output: [1]

from collections import Counter
from typing import List


class Solution:
    # time complexity O(klogn)
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # time complexity: O(n)
        # space complexity: O(n)
        # using Counter
        # return [x[0] for x in Counter(nums).most_common(k)]
        cnt = Counter(nums)

        result = []
        for i in cnt.most_common(k):
            result.append(i[0])
        return result

    # without using Counter and standard library
    # time complexity: O(nlogn) because we sorted the list
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1

        result = []
        for i in sorted(d, key=d.get, reverse=True)[:k]:
            result.append(i)
        return result


if __name__ == "__main__":
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    print(Solution().topKFrequent(nums, k))
