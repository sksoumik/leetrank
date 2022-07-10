# https://leetcode.com/problems/first-unique-character-in-a-string/
# Given a string s, find the first non-repeating character in it and
# return its index. If it does not exist, return -1.
from collections import OrderedDict, Counter


def non_repeating_character(s):
    # O(n) time, O(n) space
    counter = Counter(s)
    for idx, c in enumerate(s):
        if counter[c] == 1:
            return idx
    return -1


if __name__ == "__main__":
    s = "leetcode"
    print(non_repeating_character(s))
