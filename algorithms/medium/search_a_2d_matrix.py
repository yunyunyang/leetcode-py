# 74. Search a 2D Matrix

from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for r in matrix:
            if target >= r[0] and target <= r[-1]:
                for c in r:
                    if c == target:
                        return True
                    
        return False
    
sol = Solution().searchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13)
print(sol)