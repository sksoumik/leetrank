# https://leetcode.com/problems/palindrome-number/
# Given an integer x, return true if x is palindrome integer.
# An integer is a palindrome when it reads the same backward as forward.
# For example, 121 is a palindrome while 123 is not.


def is_palindrome(x: int):
    str_x = str(x)
    reverse_x = str_x[::-1]
    return str_x == reverse_x


if __name__ == "__main__":
    print(is_palindrome(121))
    print(is_palindrome(123))
