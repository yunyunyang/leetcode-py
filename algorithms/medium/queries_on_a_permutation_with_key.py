# 1409. Queries on a Permutation With Key

from typing import List

class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        p = [i for i in range(1, m+1)]
        o = []
        for q in queries:
            i = p.index(q)
            o.append(i)
            n = p.pop(i)
            p.insert(0, n)
        
        return o
    
sol = Solution().processQueries(queries = [3,1,2,1], m = 5)
print(sol)