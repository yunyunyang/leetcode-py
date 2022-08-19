# 2194. Cells in a Range on an Excel Sheet

from typing import List

class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        output = []
        start, end = s.split(":")
        l1, l2 = ord(start[0]), int(start[1])
        r1, r2 = ord(end[0]), int(end[1])

        for i in range(l1, r1+1):
            for j in range(l2, r2+1):
                output.append(chr(i) + str(j))
        
        return output
        
sol = Solution().cellsInRange(s = "K1:L2")
print(sol)