# 74. Search a 2D Matrix

from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, col = len(matrix), len(matrix[0])
        left, right = 0, row * col - 1
        while left <= right:
            mid = left + (right - left) // 2
            val = matrix[mid // col][mid % col]
            print(mid, val)
            if val == target:
                return True
            elif val < target:
                left = mid + 1
            elif val > target:
                right = mid - 1
                
        return False
    
sol = Solution().searchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13)
print(sol)