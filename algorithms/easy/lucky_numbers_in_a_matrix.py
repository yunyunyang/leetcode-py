# 1380. Lucky Numbers in a Matrix

from typing import List

class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        lucky = []
        min_row = set()
        for r in range(len(matrix)):
            min_row.add(min(matrix[r]))
        
        max_col = set()
        for c in range(len(matrix[0])):
            cur_max = 0
            for r in range(len(matrix)):
                if matrix[r][c] > cur_max:
                    cur_max = matrix[r][c]
            
            if cur_max in min_row:
                lucky.append(cur_max)
        
        return lucky
    
sol = Solution().luckyNumbers(matrix = [[3,7,8],[9,11,13],[15,16,17]])
print(sol)