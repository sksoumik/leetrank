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



# Symmetric Tree

https://leetcode.com/problems/symmetric-tree

Given the `root` of a binary tree, *check whether it is a mirror of itself* (i.e., symmetric around its center).

 

**Example 1:**

![img](https://assets.leetcode.com/uploads/2021/02/19/symtree1.jpg)

```
Input: root = [1,2,2,3,4,4,3]
Output: true
```

**Example 2:**

![img](https://assets.leetcode.com/uploads/2021/02/19/symtree2.jpg)

```
Input: root = [1,2,2,null,3,null,3]
Output: false
```

#### py

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root):
        if not root:
            return True
        return self.isMirror(root.left, root.right)

    def isMirror(self, left, right):
        if not left and not right:
            return True
        
        if not left or not right:
            return False
        
        return (
            left.val == right.val
            and self.isMirror(left.left, right.right)
            and self.isMirror(left.right, right.left)
        )
```



#### js

```javascript
function TreeNode(val, left, right) {
    this.val = (val === undefined ? 0 : val);
    this.left = (left === undefined ? null : left);
    this.right = (right === undefined ? null : right);
}


var isSymmetric = function (root) {
    if (!root) {
        return true;
    }
    return isMirror(root.left, root.right);
};

var isMirror = function (left, right) {
    if (!left && !right) {
        return true;
    }
    if (!left || !right) {
        return false;
    }
    return left.val === right.val &&
        isMirror(left.left, right.right) &&
        isMirror(left.right, right.left);
}
```



# Add Binary

https://leetcode.com/problems/add-binary/

Given two binary strings a and b, return their sum as a binary string.

**Example 1:**

```
Input: a = "11", b = "1"
Output: "100"
```

**Example 2:**

```
Input: a = "1010", b = "1011"
Output: "10101"
```

#### py

```python
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # Converting the binary string to an integer.
        a = int(a, 2)
        b = int(b, 2)
        # add a and b
        c = a + b
        # convert int to binary string
        return bin(c)[2:]
```



# Best Time to Buy and Sell Stock

https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

You are given an array `prices` where `prices[i]` is the price of a given stock on the `ith` day.

You want to maximize your profit by choosing a **single day** to buy one stock and choosing a **different day in the future** to sell that stock.

Return *the maximum profit you can achieve from this transaction*. If you cannot achieve any profit, return `0`.

 

**Example 1:**

```
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
```

**Example 2:**

```
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
```



#### py

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        We start with a left pointer at the beginning of the array and a right pointer at the second
        element. We then check to see if the element to the right is greater than the element to the
        left. If it is, we calculate the current profit and update our max profit if the current profit
        is greater. If the element to the right is not greater, we move the left pointer to the right by
        one. We then increment the right pointer by one. We repeat this process until the right pointer
        is at the end of the array

        :param prices: List[int] -> This is the list of prices that we are given
        :type prices: List[int]
        :return: The max profit that can be made from buying and selling a stock
        """
        max_profit = 0

        # left pointer, idx of buying the stock
        buy = 0

        # right pointer, index of selling the stock
        sell = 1

        while sell < len(prices):
            current_profit = prices[sell] - prices[buy]

            # if the buy < sell: then update max profit
            if prices[buy] < prices[sell]:
                max_profit = max(current_profit, max_profit)
            else:
                # update pointers
                buy = sell
            sell += 1

        return max_profit
```



#### js

```javascript
var maxProfit = function (prices) {
  max_profit = 0;

  buy = 0;
  sell = 1;
  while (sell < prices.length) {
    current_profit = prices[sell] - prices[buy];

    // if the sell > buy: update the max profit
    if (prices[sell] > prices[buy]) {
      max_profit = Math.max(max_profit, current_profit);
    } else {
      // if the sell < buy: update the buy
      buy = sell;
    }
    sell++;
  }
  return max_profit;
};
```



# Binary Search

Given an array of integers `nums` which is sorted in ascending order, and an integer `target`, write a function to search `target` in `nums`. If `target` exists, then return its index. Otherwise, return `-1`.

You must write an algorithm with `O(log n)` runtime complexity.

 

**Example 1:**

```
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4
```

**Example 2:**

```
Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
```



#### py

```

```

