# https://leetcode.com/problems/flood-fill/description/

# An image is represented by an m x n integer grid image 
# where image[i][j] represents the pixel value of the image.

# You are also given three integers sr, sc, and color. 
# You should perform a flood fill on the image starting from the pixel image[sr][sc].

# To perform a flood fill, consider the starting pixel, 
# plus any pixels connected 4-directionally to the starting pixel 
# of the same color as the starting pixel, plus any pixels connected
#  4-directionally to those pixels (also with the same color), and so on. 
#  Replace the color of all of the aforementioned pixels with color.

# Return the modified image after performing the flood fill.

from typing import List
from functools import lru_cache


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        # store the color of the starting pixel
        start_color = image[sr][sc]
        
        @lru_cache(maxsize=None)
        def flood_fill(x, y):  
            # x represents the row, y represents the column
            # return if the current pixel is out of bounds

            if x < 0 or x >= len(image): return None
            if y < 0 or y >= len(image[0]): return None
            
            # return if the current pixel is already the target color
            if image[x][y] == color: return None
            
            # return if the current pixel has a different color than the starting pixel
            if image[x][y] != start_color: return None
            
            # set the color of the current pixel to the target color
            image[x][y] = color
            
            # perform flood fill on the surrounding pixels
            flood_fill(x-1, y)  # top
            flood_fill(x+1, y)  # bottom
            flood_fill(x, y+1)  # right
            flood_fill(x, y-1)  # left
        
        # start the flood fill at the starting pixel
        flood_fill(sr, sc)
        return image


if __name__ == '__main__':
    # Test the solution
    image = [[1,1,1],[1,1,0],[1,0,1]]
    sr = 1
    sc = 1
    color = 2
    print(Solution().floodFill(image, sr, sc, color))  # Output: [[2,2,2],[2,2,0],[2,0,1]]
