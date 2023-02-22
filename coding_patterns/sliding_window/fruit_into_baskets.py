# https://leetcode.com/problems/fruit-into-baskets/

from typing import List

def totalFruit(fruits):
    # initialize variables
    max_fruits = 0
    basket = {}
    left = 0

    # loop through the entire tree list
    for right in range(len(fruits)):
        # If the fruit is not in the basket, get method returns 0, 
        # which means 1 will be added as the initial count of that fruit. 
        # If the fruit is already in the basket, 
        # the previous count is retrieved and incremented by 1 to reflect 
        # the addition of another fruit of the same type.
        basket[fruits[right]] = basket.get(fruits[right], 0) + 1

        # while there are more than 2 fruits in the basket, 
        # remove the leftmost fruit
        while len(basket) > 2:
            basket[fruits[left]] -= 1
            # if the count of the leftmost fruit is 0,
            # remove it from the basket 
            if basket[fruits[left]] == 0:
                del basket[fruits[left]]
            # increment the left pointer
            left += 1

        # The length of the current subarray is calculated by subtracting 
        # the left pointer from the right pointer and adding 1 to the result. 
        # This is because the subarray is defined as the range of indices 
        # from left to right, inclusive.
        max_fruits = max(max_fruits, right - left + 1)

    return max_fruits



if __name__ == "__main__":
    tree = [1, 2, 1]
    max_fruits = totalFruit(tree)
    print(max_fruits) # 3

    tree = [0, 1, 2, 2]
    max_fruits = totalFruit(tree)
    print(max_fruits) # 3

