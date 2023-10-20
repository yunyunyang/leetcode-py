# 2022. Convert 1D Array Into 2D Array

from typing import List


class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        twodarray = []

        l, r = 0, n
        while r <= len(original):
            if m * n != len(original):
                return twodarray

            twodarray.append(original[l:r])
            l += n
            r += n

            if len(twodarray) > m:
                return twodarray

        return twodarray


sol = Solution().construct2DArray(original=[5], m=3, n=1)
print(sol)
