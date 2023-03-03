# 1828. Queries on Number of Points Inside a Circle

from typing import List

class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        o = [0] * len(queries)
        for i in range(len(queries)):
            for x, y in points:                
                d = pow((queries[i][0]-x)**2 + (queries[i][1]-y)**2, 0.5)
                if d <= queries[i][2]:
                    o[i] += 1
            
        return o
    

sol = Solution().countPoints([[1,3],[3,3],[5,3],[2,2]], queries = [[2,3,1],[4,3,1],[1,1,2]])
print(sol)