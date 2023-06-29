# 2643. Row With Maximum Ones

from typing import List

class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        m, n = 0, 0
        for i in range(len(mat)-1, -1, -1):
            j = sum(mat[i])
            if j >= n:
                m = i
                n = j

        return [m, n]
    
sol = Solution().rowAndMaximumOnes(mat = [[0],[0]])
print(sol)