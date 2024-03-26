# 41. First Missing Positive
from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nmap = {}
        for n in nums:
            nmap[n-1] = n

        print(nmap)

        for i in range(len(nums)):
            if nmap.get(i) != i + 1:
                return i + 1

        return len(nums) + 1


sol = Solution().firstMissingPositive(nums=[3, 4, -1, 1])
print(sol)
