# implement binary search
def fn_binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if target == arr[mid]:
            # means we found the target, and return the index of the target
            return mid
        # if the target is in the right half of the array
        elif target > arr[mid]:
            left = mid + 1
        # if the target is in the left half of the array
        else:
            right = mid - 1
    # if the target is not in the array
    return -1


# implement the binary search with recursion
def fn_binary_search_recursion(arr, target, left, right):
    # base case: if the element is not in the array
    if left > right:
        return -1
    # if the element is in the array
    mid = (left + right) // 2
    if target == arr[mid]:
        return mid
    # if the target is in the right half of the array
    elif target > arr[mid]:
        return fn_binary_search_recursion(arr, target, mid + 1, right)
    # if the target is in the left half of the array
    else:
        return fn_binary_search_recursion(arr, target, left, mid - 1)


if __name__ == "__main__":
    print(fn_binary_search([1, 3, 5, 6], 5))
    print(fn_binary_search([1, 3, 5, 6], 2))

    # recursion test
    array = [1, 3, 5, 6]
    target = 5
    left, right = 0, len(array) - 1
    print(fn_binary_search_recursion(array, target, left, right))
