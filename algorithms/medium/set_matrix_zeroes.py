# 73. Set Matrix Zeroes

from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rlen, clen = len(matrix), len(matrix[0])
        for r in range(rlen):
            for c in range(clen):
                if matrix[r][c] == 0:
                    print(f"{r},{c}")
                    # update row
                    for cc in range(clen):
                        if matrix[r][cc] != 0:
                            matrix[r][cc] = '*'
                    # update column
                    for rr in range(rlen):
                        if matrix[rr][c] != 0:
                            matrix[rr][c] = '*'

        for i in range(rlen):
            for j in range(clen):
                if matrix[i][j] == '*':
                    matrix[i][j] = 0

        print(matrix)


sol = Solution().setZeroes(matrix=[[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]])
