# 1817. Finding the Users Active Minutes

from typing import List

class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        o = [0]*k
        d = {}
        for k, v in logs:
            if k not in d:
                d[k] = {v}
            else:
                d[k].add(v)
            
        print(d)
        for k, v in d.items():
            s = len(v)
            o[s-1] += 1

        return o
    
sol = Solution().findingUsersActiveMinutes(logs = [[0,5],[1,2],[0,2],[0,5],[1,3]], k = 5)
print(sol)