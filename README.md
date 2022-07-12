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

https://leetcode.com/problems/binary-search/

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

```python
class Solution:
    def search(self, nums: List[int], target: int):
        i, j = 0, len(nums) - 1
        while i <= j:
            idx_of_mid = (i + j) // 2
            mid_element = nums[idx_of_mid]

            if target == mid_element:
                return idx_of_mid
            if target > mid_element:
                i = idx_of_mid + 1
            else:
                j = idx_of_mid - 1
        
        return -1
```

#### js

```javascript
var search = function (nums, target) {
  let i = 0;
  let j = nums.length - 1;
  while (i <= j) {
    let idx_of_mid = Math.floor((i + j) / 2);
    let mid_element = nums[idx_of_mid];
    if (target === mid_element) {
      return idx_of_mid;
    }
    if (target > mid_element) {
      i = idx_of_mid + 1;
    } else {
      j = idx_of_mid - 1;
    }
  }
  return -1;
};
```



# Binary Tree Inorder Traversal

https://leetcode.com/problems/binary-tree-inorder-traversal/

Given the `root` of a binary tree, return *the inorder traversal of its nodes' values*.

 

**Example 1:**

![img](https://assets.leetcode.com/uploads/2020/09/15/inorder_1.jpg)

```
Input: root = [1,null,2,3]
Output: [1,3,2]
```

**Example 2:**

```
Input: root = []
Output: []
```

**Example 3:**

```
Input: root = [1]
Output: [1]
```



#### py

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root):
        if root is None:
            return []
        return (
            self.inorderTraversal(root.left)
            + [root.val]
            + self.inorderTraversal(root.right)
        )
```



#### js

```javascript
function TreeNode(val, left, right) {
  this.val = val === undefined ? 0 : val;
  this.left = left === undefined ? null : left;
  this.right = right === undefined ? null : right;
}

var inorderTraversal = function (root) {
  // if root is null, return an empty array
  if (!root) return [];
  // if root is not null, return the inorder traversal of the left subtree
  // concatenated with the root's value
  // concatenated with the inorder traversal of the right subtree
  return inorderTraversal(root.left)
    .concat(root.val)
    .concat(inorderTraversal(root.right));
};

// main 
console.log(
  inorderTraversal(
    new TreeNode(
      1,
      new TreeNode(2, new TreeNode(4), new TreeNode(5)),
      new TreeNode(3, new TreeNode(6), new TreeNode(7))
    )
  )
);
```



# Climbing Stairs

https://leetcode.com/problems/climbing-stairs

You are climbing a staircase. It takes `n` steps to reach the top.

Each time you can either climb `1` or `2` steps. In how many distinct ways can you climb to the top?

 

**Example 1:**

```
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
```

**Example 2:**

```
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
```



#### py

```python
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
```

#### js

```

```



# Contains Duplicate

https://leetcode.com/problems/contains-duplicate

Given an integer array `nums`, return `true` if any value appears **at least twice** in the array, and return `false` if every element is distinct.

 

**Example 1:**

```
Input: nums = [1,2,3,1]
Output: true
```

**Example 2:**

```
Input: nums = [1,2,3,4]
Output: false
```

**Example 3:**

```
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
```



#### py

```python
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        If the length of the list of unique values is not equal to the length of the original list, then
        there are duplicates
        
        :param nums: List[int] -> this is the list of numbers that we're going to be checking for
        duplicates
        :type nums: List[int]
        :return: A boolean value.
        """
        unique_values = list(set(nums))

        if len(unique_values) != len(nums):
            return True
        else:
            return False
```



# Diameter of Binary Tree

https://leetcode.com/problems/diameter-of-binary-tree/

Given the `root` of a binary tree, return *the length of the **diameter** of the tree*.

The **diameter** of a binary tree is the **length** of the longest path between any two nodes in a tree. This path may or may not pass through the `root`.

The **length** of a path between two nodes is represented by the number of edges between them.

 

**Example 1:**

![img](https://assets.leetcode.com/uploads/2021/03/06/diamtree.jpg)

```
Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].
```

**Example 2:**

```
Input: root = [1,2]
Output: 1
```



#### py

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root):
        """
        The diameter of a binary tree is the maximum of the following three numbers:

        1. The diameter of the left subtree.
        2. The diameter of the right subtree.
        3. The longest path between any two nodes in the left subtree + the longest path between any two
        nodes in the right subtree

        :param root: the root of the tree
        :return: The diameter of the tree.
        """
        if root is None:
            return 0
        return max(
            self.diameterOfBinaryTree(root.left),
            self.diameterOfBinaryTree(root.right),
            self.maxDepth(root.left) + self.maxDepth(root.right),
        )

    def maxDepth(self, root):
        """
        The maximum depth of a binary tree is the maximum number of nodes along the path from the root
        node down to the farthest leaf node

        :param root: the root node of the tree
        :return: The max depth of the tree.
        """
        if root is None:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
```

