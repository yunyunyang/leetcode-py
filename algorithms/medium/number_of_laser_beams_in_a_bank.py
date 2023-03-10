# 2125. Number of Laser Beams in a Bank

from typing import List

class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        o, n = 0, 0
        for b in bank:
            t = b.count('1')
            if t > 0:
                o += n*t
                n = t
        return o

sol = Solution().numberOfBeams(bank = ["011001","000000","010100","001000"])
print(sol)