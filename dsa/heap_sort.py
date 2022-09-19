"""
ref: https://www.geeksforgeeks.org/heap-sort/
"""

# Python program for implementation of heap Sort
# To heapify subtree rooted at index i.
# n is size of heap
# time O(n log n)
# space O(1)


# do the max heapify operation
def heapify(arr, n, i):
    """
    If the root is not the largest, swap the root with the largest child and heapify the new root.

    :param arr: The array to be sorted
    :param n: the size of the array
    :param i: index of the current node
    """
    largest = i  # Initialize largest as root
    l = 2 * i + 1  # left = 2*i + 1
    r = 2 * i + 2  # right = 2*i + 2

    # See if left child of root exists and is
    # greater than root
    if l < n and arr[i] < arr[l]:
        largest = l

    # See if right child of root exists and is
    # greater than root
    if r < n and arr[largest] < arr[r]:
        largest = r

    # Change root, if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap

        # Heapify the root.
        heapify(arr, n, largest)


# The main function to sort an array of given size
def heapSort(arr):
    n = len(arr)

    # Build a maxheap.
    for i in range(n, -1, -1):
        heapify(arr, n, i)

    # One by one extract elements
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)


if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6, 7]
    print("Given array is")
    print(arr)
    heapSort(arr)
    print("Sorted array is")
    print(arr)
