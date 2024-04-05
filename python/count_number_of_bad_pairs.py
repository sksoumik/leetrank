# https://leetcode.com/count-number-of-bad-pairs

# You are given a 0-indexed integer array nums.
# A pair of indices (i, j) is a bad pair if i < j and j - i != nums[j] - nums[i].

# Return the total number of bad pairs in nums.

# Input: nums = [4,1,3,3]
# Output: 5


from collections import Counter


class Solution:

    # brute force
    def countBadPairs_bf(self, nums):
        count = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if i < j and nums[j] - nums[i] != j - i:
                    count += 1
        return count

    def countBadPairs(self, nums):
        length = len(nums)
        result = []

        for i in range(length):
            result.append(nums[i] - i)

        print(result)
        counter = Counter(result)
        print(counter)

        answer = length * (length - 1) // 2

        print(answer)

        for x in counter:
            answer -= counter[x] * (counter[x] - 1) // 2
        return answer


if __name__ == "__main__":
    nums = [4, 1, 3, 3]
    s = Solution()
    print(s.countBadPairs(nums))

    # nums = [1, 2, 3, 4, 5]
    # print(s.countBadPairs(nums))
