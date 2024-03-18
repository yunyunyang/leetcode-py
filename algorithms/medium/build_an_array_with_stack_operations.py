# 1441. Build an Array With Stack Operations

from typing import List


class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        ops = []
        idx = 0
        for i in range(1, n+1):
            if idx > len(target) - 1:
                break

            ops.append('Push')
            if target[idx] != i:
                ops.append('Pop')
            else:
                idx += 1

        return ops


sol = Solution().buildArray(target=[1, 3], n=3)
print(sol)
