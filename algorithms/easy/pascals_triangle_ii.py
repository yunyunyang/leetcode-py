# 119. Pascal's Triangle II

from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        triangle = []
        for i in range(rowIndex + 1):
            if i == 0:
                triangle.append([1])
            elif i == 1:
                triangle.append([1, 1])
            else:
                row = [1]
                for j in range(i - 1):
                    row.append(triangle[i-1][j] + triangle[i-1][j+1])
                row.append(1)
                triangle.append(row)

        return triangle[-1]


sol = Solution().getRow(rowIndex=3)
print(sol)
