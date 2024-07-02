# 1550. Three Consecutive Odds

from typing import List

class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        count = 0
        for n in arr:
            if n % 2 == 1:
                count += 1
            else:
                count = 0
                
            if count == 3:
                return True
            
        return False
    
sol = Solution().threeConsecutiveOdds(arr = [2,6,4,1])
print(sol)