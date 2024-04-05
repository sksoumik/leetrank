# https://leetcode.com/problems//valid-perfect-square/

# Given a positive integer num, write a function which returns True if num is a perfect square else False.
# Follow up: Do not use any built-in library function such as sqrt.

# Input: num = 16
# Output: true


# approach: binary search
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True
        left, right = 1, num
        while left <= right:
            mid = (left + right) // 2
            if mid * mid == num:
                return True
            elif mid * mid < num:
                left = mid + 1
            else:
                right = mid - 1
        return False


# approach: built-in function
# class Solution:
#     def isPerfectSquare(self, num: int) -> bool:
#         a = math.sqrt(num)
#         return a == int(a)


if __name__ == "__main__":
    s = Solution()
    print(s.isPerfectSquare(16))
    print(s.isPerfectSquare(14))
    print(s.isPerfectSquare(1))
    print(s.isPerfectSquare(2))
    print(s.isPerfectSquare(3))
    print(s.isPerfectSquare(4))
    print(s.isPerfectSquare(5))
    print(s.isPerfectSquare(6))
    print(s.isPerfectSquare(7))
