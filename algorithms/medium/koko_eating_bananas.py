# 875. Koko Eating Bananas

from typing import List
import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        output = right
        while left <= right:
            mid = left + (right - left) // 2
            hours = 0
            for p in piles:
                hours += math.ceil(p / mid)

            if hours <= h:
                output = min(output, mid)
                right = mid - 1
            else:
                left = mid + 1

        return output

    
sol = Solution().minEatingSpeed(piles = [3,6,7,11], h = 8)
print(sol)