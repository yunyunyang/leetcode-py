# 342. Power of Four

import math


class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if (n > 0) and (n & (n - 1) == 0):
            m = 0
            while n > 1:
                m += 1
                n >>= 1
            return m % 2 == 0
        return False

        # return n > 0 and math.log(n, 4).is_integer()


sol = Solution().isPowerOfFour(n=64)
print(sol)
