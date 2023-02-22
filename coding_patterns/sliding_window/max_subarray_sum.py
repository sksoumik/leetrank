"""
Given an array arr and a positive integer k, 
find the maximum sum of any contiguous subarray of size k.

Write a function max_subarray_sum(arr, k) that takes 
an array arr and a positive integer k as input and returns 
an integer representing  the maximum sum of any contiguous 
subarray of size k.
"""

def max_subarray_sum(arr, k):   # k = window size
    n = len(arr)
    # checks if the length of the array is less than k (window size), 
    # in which case it returns an "Invalid Input" message.
    if n < k:
        return "Invalid Input"
    
    # initialize the max_sum and current_sum variables
    # max_sum is initialized to the sum of the first k elements of the array
    max_sum = sum(arr[0: k])
    current_sum = max_sum

    for i in range(k, n):
        # current_sum is updated by subtracting the first element of the
        # previous window and adding the next element of the current window
        current_sum += arr[i] - arr[i - k]
        # max_sum is updated by comparing the current_sum and max_sum
        max_sum = max(max_sum, current_sum)
    
    return max_sum


if __name__ == "__main__":
    arr = [1, 4, 2, 10, 2, 3, 1, 0, 20]
    k = 4
    max_sum = max_subarray_sum(arr, k)
    print(max_sum)    
    # 24;  becase 3+1+0+20 = 24