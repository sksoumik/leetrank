### Resources / Explanations

#### Videos
 - [Top 5 Dynamic Programming Patterns for Coding Interviews](https://youtu.be/mBNrRy2_hVs)

 - [How to solve (almost) any binary tree coding problem](https://youtu.be/s2Yyk3qdy3o)

 - 


#### Blogs
 - [Best practice questions](https://www.techinterviewhandbook.org/best-practice-questions/)
 - [Grind 75 questions](https://www.techinterviewhandbook.org/grind75)
 - [LEETCODE PATTERNS](https://seanprashad.com/leetcode-patterns/)
 - [Coding interview cheatsheet: Best practices before, during and after](https://www.techinterviewhandbook.org/coding-interview-cheatsheet/)
 - [The 30 most common Software Engineer behavioral interview questions](https://www.techinterviewhandbook.org/behavioral-interview-questions/)



# Two Sum

https://leetcode.com/problems/two-sum/

Given an array of integers `nums` and an integer `target`, return *indices of the two numbers such that they add up to `target`*.

You may assume that each input would have ***exactly\* one solution**, and you may not use the *same* element twice.

You can return the answer in any order.

 

**Example 1:**

```
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
```



#### py

```python
def two_sum_bf(arr, target):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == target:
                return [i, j]
    return []


# method 2: O (n) solution: hash table
def two_sum_hash(arr, target):
    hash_table = {}  # key: num, value: index
    for idx, num in enumerate(arr):
        complement = target - num
        if complement in hash_table:
            return [hash_table[complement], idx]
        hash_table[num] = idx
    
    return []
```



#### js

```javascript
var twoSum = function (nums, target) {
    let hash_table = {};
    for (let i = 0; i < nums.length; i++) {
        let complement = target - nums[i];
        if (complement in hash_table) {
            return [hash_table[complement], i];
        }
        hash_table[nums[i]] = i;
    }

};
```



