# 1863. Sum of All Subset XOR Totals

from typing import List

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        r = [[]]
        for i in nums:
            r += [s + [i] for s in r]

        o = 0
        for i in range(1, len(r)):
            t = r[i][0]
            for j in range(1, len(r[i])):
                t ^= r[i][j]
            o += t

        return o
    
sol = Solution().subsetXORSum(nums = [1,3])
print(sol)