# https://leetcode.com/problems/two-sum/

# method 1: O (n^2) brute force solution
def two_sum_bf(arr, target):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == target:
                return [i, j]
    return []


# method 2: O (n) solution: hash table
def two_sum_hash(arr, target):
    hash_table = {}
    for idx, num in enumerate(arr):
        complement = target - num
        if complement in hash_table:
            return [hash_table[complement], idx]
        hash_table[num] = idx
    return []


if __name__ == "__main__":
    # test case 1
    nums = [2, 7, 11, 15]
    target = 9
    print(two_sum_hash(nums, target))

    # test case 2
    nums = [3, 2, 4]
    target = 6
    print(two_sum_hash(nums, target))

    # test case 3
    nums = [3, 3]
    target = 6
    print(two_sum_hash(nums, target))
