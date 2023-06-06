# 1502. Can Make Arithmetic Progression From Sequence

from typing import List

class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        d = arr[1] - arr[0]
        for i in range(2, len(arr)):
            if arr[i] - arr[i-1] != d:
                return False
            
        return True
    
sol = Solution().canMakeArithmeticProgression(arr = [1,2,4])
print(sol)