# 3075. Maximize Happiness of Selected Children

from typing import List

class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort()
        max_happiness, i = 0, 0 
        while i < k:
            happy = 0 if happiness[-1] - i < 0 else happiness.pop() - i
            max_happiness += happy
            i += 1

        return max_happiness
    
sol = Solution().maximumHappinessSum(happiness = [2,3,4,5], k = 1)
print(sol)