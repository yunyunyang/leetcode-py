# 2859. Sum of Values at Indices With K Set Bits

from typing import List


class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        ans = 0
        for i, n in enumerate(nums):
            if bin(i).count('1') == k:
                ans += n

        return ans


sol = Solution().sumIndicesWithKSetBits(nums=[5, 10, 1, 5, 2], k=1)
print(sol)
