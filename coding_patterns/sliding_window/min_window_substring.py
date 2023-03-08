# https://leetcode.com/problems/minimum-window-substring/


# brute force solution

# The brute force solution to the problem of finding the minimum window substring of s 
# that contains all the characters of t would involve generating all possible substrings
# of s and checking if each substring contains all the characters of t. We would then keep track of the
# minimum length and minimum window substring that contains all the characters of t.


# time complexity O(n^2 * m)
# the method generates all possible substrings of s using nested loops, which takes O(n^2) time. 
# For each substring, it checks if it contains all the characters of t using the contains_all_chars
# method, which takes O(m) time, where m is the length of t. Hence, the overall time complexity 
# is O(n^2 * m).
class Solution:
    def minWindow_bf(self, s: str, t: str) -> str:
        min_len = float('inf')
        min_window = ""

        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                window = s[i:j]
                if self.contains_all_chars(window, t):
                    if len(window) < min_len:
                        min_len = len(window)
                        min_window = window

        return min_window

    def contains_all_chars(self, window, t):
        for char in t:
            if char not in window:
                return False
        return True
    


    

# sliding window using two pointers
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        




    
               


