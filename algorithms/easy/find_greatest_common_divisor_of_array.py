# 1979. Find Greatest Common Divisor of Array

from typing import List


class Solution:
    def findGCD(self, nums: List[int]) -> int:
        m, n = max(nums), min(nums)
        while m != 0 and n != 0:
            if m // n > 0:
                q = n
            r = m % n
            m, n = n, r

        return max(m, n)


sol = Solution().findGCD(nums=[2, 5, 6, 9, 10])
print(sol)
