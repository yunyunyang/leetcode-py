# 2161. Partition Array According to Given Pivot

from typing import List

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        l = []
        e = []
        g = []
        for i in nums:
            if i == pivot:
                e.append(i)
            elif i < pivot:
                l.append(i)
            elif i > pivot:
                g.append(i)
                
        return l + e + g
    
sol = Solution().pivotArray(nums = [9,12,5,10,14,3,10], pivot = 10)
print(sol)