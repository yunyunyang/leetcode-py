# 2391. Minimum Amount of Time to Collect Garbage

from typing import List

class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        output, idx_p, idx_g, idx_m = 0, 0, 0, 0

        for i, g in enumerate(garbage):
            if 'P' in g:
                output += g.count('P')
                if i > idx_p: 
                    idx_p = i

        for i, g in enumerate(garbage):
            if 'G' in g:
                output += g.count('G')
                if i > idx_g: 
                    idx_g = i

        for i, g in enumerate(garbage):
            if 'M' in g:
                output += g.count('M')
                if i > idx_m: 
                    idx_m = i 
            
        output += sum(travel[0:idx_p])
        output += sum(travel[0:idx_g])
        output += sum(travel[0:idx_m])

        return output


sol = Solution().garbageCollection(garbage = ["G","P","GP","GG"], travel = [2,4,3])
print(sol)