# 1460. Make Two Arrays Equal by Reversing Subarrays

from typing import List

class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        tmap, amap = {}, {}
        
        for i in range(len(target)):
            t, a = target[i], arr[i]
            tmap[t] = tmap.get(t, 0) + 1
            amap[a] = amap.get(a, 0) + 1
        
        return tmap == amap
    
sol = Solution().canBeEqual(target = [1,2,3,4], arr = [2,4,1,3])
print(sol)