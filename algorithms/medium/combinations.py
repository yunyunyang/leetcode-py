# 77. Combinations

from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        output = []
        
        def backtrack(start, comb):        
            if len(comb) == k:
                output.append(comb.copy())
                return
            
            for i in range(start, n + 1):
                comb.append(i)
                backtrack(i + 1, comb)
                comb.pop()
        
        backtrack(1, [])
        return output

sol = Solution().combine(n = 4, k = 2)
print(sol)