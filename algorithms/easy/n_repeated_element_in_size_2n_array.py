# 961. N-Repeated Element in Size 2N Array

from typing import List


class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        num = len(nums) / 2
        times = {}
        for n in nums:
            if n not in times:
                times[n] = 1
            elif times[n] == num - 1:
                return n
            else:
                times[n] += 1


sol = Solution().repeatedNTimes(nums=[1, 2, 3, 3])
print(sol)
