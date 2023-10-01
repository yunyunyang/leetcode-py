# 896. Monotonic Array

from typing import List


class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return True

        flags = set()
        for i in range(1, len(nums)):
            n = nums[i] - nums[i - 1]
            if n > 0:
                flags.add(True)
            elif n < 0:
                flags.add(False)

            if len(flags) >= 2:
                return False

        return len(flags) <= 1


sol = Solution().isMonotonic(nums=[1, 2, 4, 3])
print(sol)
