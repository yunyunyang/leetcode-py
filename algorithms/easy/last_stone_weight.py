# 1046. Last Stone Weight

from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]
        
        stones.sort()
        while len(stones) > 1:
            m = stones.pop(-1)
            n = stones.pop(-1)
            stones.append(m-n)
            stones.sort()

        return stones[0]
    
sol = Solution().lastStoneWeight(stones = [2,7,4,1,8,1])
print(sol)