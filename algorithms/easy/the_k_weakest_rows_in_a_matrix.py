# 1337. The K Weakest Rows in a Matrix

from typing import List


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        s = []
        for i, m in enumerate(mat):
            s.append((i, sum(m)))

        s = sorted(s, key=lambda k: k[1])
        o = []
        for i in range(len(s)):
            o.append(s[i][0])
            if i == k-1:
                return o


mat = \
    [[1, 1, 0, 0, 0],
     [1, 1, 1, 1, 0],
        [1, 0, 0, 0, 0],
        [1, 1, 0, 0, 0],
        [1, 1, 1, 1, 1]],

sol = Solution().kWeakestRows(mat, k=3)
print(sol)
