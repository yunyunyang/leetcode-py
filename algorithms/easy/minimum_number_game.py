# 2974. Minimum Number Game

from typing import List


class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        nums.sort()
        for i in range(0, len(nums), 2):
            n = nums[i]
            nums[i] = nums[i+1]
            nums[i+1] = n

        return nums


sol = Solution().numberGame(nums=[5, 4, 2, 3])
print(sol)
