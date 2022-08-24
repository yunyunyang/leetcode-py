# 326. Power of Three

import math


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        else:
            while n % 3 == 0:
                n /= 3

            return n == 1

sol = Solution().isPowerOfThree(n = 243)
print(sol)