# 1281. Subtract the Product and Sum of Digits of an Integer

import math

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        ns = [int(i) for i in str(n)]
        return math.prod(ns) - sum(ns)

sol = Solution().subtractProductAndSum(n = 234)
print(sol)