# 1791. Find Center of Star Graph

from typing import List

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        output = 0
        x, y = edges[0][0], edges[0][1]
        for i in edges:
            if x in i:
                output = x
            if y in i:
                output = y
            
        return output

sol = Solution().findCenter(edges = [[1,2],[5,1],[1,3],[1,4]])
print(sol)