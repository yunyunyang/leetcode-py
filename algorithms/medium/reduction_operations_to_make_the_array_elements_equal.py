# 1887. Reduction Operations to Make the Array Elements Equal

from typing import List


class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        n, ops = len(nums), 0
        nums.sort()
        for i in range(0, n-1):
            if nums[i] != nums[i+1]:
                ops += n - i - 1

        return ops


sol = Solution().reductionOperations(nums=[5, 1, 3])
print(sol)
