# 905. Sort Array By Parity

from typing import List


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        l, r = 0, len(nums) - 1
        while l < r:
            if l < r and nums[l] % 2 == 0:
                l += 1
            if l < r and nums[r] % 2 != 0:
                r -= 1

            nums[l], nums[r] = nums[r], nums[l]

        return nums


sol = Solution().sortArrayByParity(nums=[0, 1])
print(sol)
