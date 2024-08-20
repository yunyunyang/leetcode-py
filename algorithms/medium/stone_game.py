# 877. Stone Game

from typing import List
from collections import deque

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        piles = deque(piles)
        alice, bob = 0, 0

        while piles:
            left, right = piles.popleft(), piles.pop()
            m = max(left, right)
            n = min(left, right)
            alice += m
            bob += n

        return alice > bob
    
sol = Solution().stoneGame(piles = [5,3,4,5])
print(sol)