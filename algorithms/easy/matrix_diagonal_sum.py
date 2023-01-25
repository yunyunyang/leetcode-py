# 1572. Matrix Diagonal Sum

from typing import List

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        if n == 1:
            return mat[0][0]
        else:
            diagonal_sum = 0
            c = n // 2
            for i in range(n):
                diagonal_sum += mat[i][i] + mat[i][n-(i+1)]
                
        return diagonal_sum if n%2 == 0 else diagonal_sum - mat[c][c]
    

sol = Solution().diagonalSum(mat = [[1,2,3],[4,5,6],[7,8,9]])
print(sol)