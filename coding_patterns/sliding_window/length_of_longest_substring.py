def length_of_longest_substring(s):
    n = len(s)
    if n <= 1:
        return n

    # window to keep track of the unique characters in the current window
    window = set()

    # left and right to define the boundaries of the window.
    left, right = 0, 0

    # max length seen far
    max_len = 0

    # while loop that continues until the right pointer reaches the end 
    # of the string. 
    while right < n:
        # if the character at the right pointer is not already in the window, 
        # it is added to the window
        if s[right] not in window:
            window.add(s[right])
            # increment the right pointer
            right += 1
            # compare the max length
            max_len = max(max_len, right - left)
        else:
            # If the character is already in the window, 
            # it is removed from the window,
            window.remove(s[left])
            # increment the left pointer
            left += 1

    return max_len

if __name__ == "__main__":
    strs = "abcabcbb"
    max_len = length_of_longest_substring(strs)
    print(max_len) 