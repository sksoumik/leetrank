# https://leetcode.com/problems/palindrome-number/
# Given an integer x, return true if x is palindrome integer.
# An integer is a palindrome when it reads the same backward as forward.
# For example, 121 is a palindrome while 123 is not.


def is_palindrome(x: int):
    str_x = str(x)
    reverse_x = str_x[::-1]
    return str_x == reverse_x

#without converting to string
def is_palindrome2(x: int):
    # any negative number is not a palindrome
    if x < 0:
        return False

    reverse = 0
    original = x
    while x > 0:
        # Adding the last digit of x to the reverse variable.
        reverse = reverse * 10 + x % 10
        # The same as `x = x // 10`
        x = x // 10

    return reverse == original



if __name__ == "__main__":
    # print(is_palindrome(121))
    # print(is_palindrome(123))
    print(is_palindrome2(121))
