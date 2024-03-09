# 1561. Maximum Number of Coins You Can Get

from typing import List


class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        end = int(len(piles) - (len(piles) / 3))
        max_coins = 0
        for i in range(1, end, 2):
            max_coins += piles[i]

        return max_coins


sol = Solution().maxCoins(piles=[9, 8, 7, 6, 5, 1, 2, 3, 4])
print(sol)
