# You are given two 2D integer arrays, items1 and items2, representing two sets of items. Each array items has the following properties:

# items[i] = [valuei, weighti] where valuei represents the value and weighti represents the weight of the ith item.
# The value of each item in items is unique.
# Return a 2D integer array ret where ret[i] = [valuei, weighti], with weighti being the sum of weights of all items with value valuei.

# Note: ret should be returned in ascending order by value.

# Input: items1 = [[1,1],[4,5],[3,8]], items2 = [[3,1],[1,5]]
# Output: [[1,6],[3,9],[4,5]]
# Explanation: 
# The item with value = 1 occurs in items1 with weight = 1 and in items2 with weight = 5, total weight = 1 + 5 = 6.
# The item with value = 3 occurs in items1 with weight = 8 and in items2 with weight = 1, total weight = 8 + 1 = 9.
# The item with value = 4 occurs in items1 with weight = 5, total weight = 5.  
# Therefore, we return [[1,6],[3,9],[4,5]].

from typing import List

class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        # sort by value
        items1.sort(key=lambda x: x[0])
        items2.sort(key=lambda x: x[0])
        # merge
        i, j = 0, 0
        ret = []
        while i < len(items1) and j < len(items2):
            if items1[i][0] == items2[j][0]:
                ret.append([items1[i][0], items1[i][1] + items2[j][1]])
                i += 1
                j += 1
            elif items1[i][0] < items2[j][0]:
                ret.append(items1[i])
                i += 1
            else:
                ret.append(items2[j])
                j += 1
        while i < len(items1):
            ret.append(items1[i])
            i += 1
        while j < len(items2):
            ret.append(items2[j])
            j += 1
        return ret
    

if __name__ == "__main__":
    s = Solution()
    items1 = [[1,1],[4,5],[3,8]]
    items2 = [[3,1],[1,5]]
    print(s.mergeSimilarItems(items1, items2))

    items1 = [[1,1],[3,2],[2,3]]
    items2 = [[2,1],[3,2],[1,3]]
    print(s.mergeSimilarItems(items1, items2))
    