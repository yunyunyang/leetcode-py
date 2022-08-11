# 1431. Kids With the Greatest Number of Candies
from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        greatest = max(candies)
        return [True if candy + extraCandies >= greatest else False for candy in candies]


sol = Solution().kidsWithCandies(candies = [2,3,5,1,3], extraCandies = 3)
print(sol)