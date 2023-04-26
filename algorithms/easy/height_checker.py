# 1051. Height Checker

from typing import List

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sh = sorted(heights)
        return sum([0 if heights[i] == sh[i] else 1 for i in range(len(heights))])
    
sol = Solution().heightChecker(heights = [1,1,4,2,1,3])
print(sol)