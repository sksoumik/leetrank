# Given an array of integers of size ‘n’, Our aim is to calculate the
# maximum sum of ‘k’ consecutive elements in the array.

from matplotlib.pyplot import pink


def get_maximum_sum(arr, k):
    """
    Slidigg window technique to find the maximum sum of k elements from the array

    k: window size -> k consecutive elements
    arr: given an array of integers of size ‘n’

    arr = [1, 4, 2, 10, 2, 3, 1, 0, 20]
    k = 3

    1: [1, 4, 2]   = 7
    2: [4, 2, 10]  = 16
    ...
    """
    # lenth of the array
    n = len(arr)

    # if the winddow size is less than the array size then return invalid
    if k > n:
        return -1

    # find the initial sum of k elements
    max_sum = float("-inf")

    # sliding window, move the window one by one
    for i in range(n - k + 1):
        window_sum = sum(arr[i : i + k])
        max_sum = max(max_sum, window_sum)
    return max_sum


if __name__ == "__main__":
    arr = [1, 4, 2, 10, 2, 3, 1, 0, 20]
    k = 4
    print(get_maximum_sum(arr, k))
