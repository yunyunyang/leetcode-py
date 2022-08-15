# Richest Customer Wealth

from typing import List

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max = 0
        for items in accounts:
            tmp = sum(items)
            if tmp > max:
                max = tmp

        return max

sol = Solution().maximumWealth(accounts = [[1,5],[7,3],[3,5]])
print(sol)