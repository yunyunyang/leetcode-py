# 2482. Difference Between Ones and Zeros in Row and Column

from typing import List


class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        row, col = len(grid), len(grid[0])
        onerow, onecol = [0]*row, [0]*col
        matrix = [[0] * col for _ in range(row)]

        for i in range(row):
            for j in range(col):
                onerow[i] += grid[i][j]
                onecol[j] += grid[i][j]

        for i in range(row):
            for j in range(col):
                matrix[i][j] = 2 * (onerow[i] + onecol[j]) - row - col

        return matrix


sol = Solution().onesMinusZeros(grid=[[0, 1, 1], [1, 0, 1], [0, 0, 1]])
print(sol)
