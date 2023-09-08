# 118. Pascal's Triangle

from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        o = [[1]]
        for i in range(1, numRows):
            n = [1]
            for j in range(1, i):
                print(j)
                n.append(sum(o[-1][j-1:j+1]))
            n.append(1)
            o.append(n)

        return o


sol = Solution().generate(numRows=5)
print(sol)
