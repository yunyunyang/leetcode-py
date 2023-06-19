# 1732. Find the Highest Altitude

from typing import List

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        o, a = 0, 0
        for i in gain:
            a += i
            o = max(a, o)
       
        return o
    
sol = Solution().largestAltitude(gain = [-4,-3,-2,-1,4,3,2])
print(sol)