# 442. Find All Duplicates in an Array

from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        s = set()
        dupes = []
        for n in nums:
            if n not in s:
                s.add(n)
            else:
                dupes.append(n)

        return dupes


sol = Solution().findDuplicates(nums=[1, 1, 2])
print(sol)
