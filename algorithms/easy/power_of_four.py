# 342. Power of Four

import math

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n > 0 and math.log(n, 4).is_integer()

sol = Solution().isPowerOfFour(n = -64)
print(sol)