# 1833. Maximum Ice Cream Bars

from typing import List

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        o = 0
        costs.sort()
        for i in costs:
            if coins >= i:
                coins -= i
                o +=1
            else:
                continue
        
        print(coins)
        return o
    
sol = Solution().maxIceCream(costs = [1,3,2,4,1], coins = 7)
print(sol)