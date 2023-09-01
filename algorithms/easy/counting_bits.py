# 338. Counting Bits

from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        o = [0] * (n + 1)
        offset = 1
        for i in range(1, n + 1):
            if offset * 2 == i:
                offset = i

            o[i] = 1 + o[i - offset]

        return o


sol = Solution().countBits(n=2)
print(sol)
