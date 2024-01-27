# 2824. Count Pairs Whose Sum is Less than Target

from typing import List


class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        pairs, left, right = 0, 0, len(nums)-1
        nums.sort()

        while left < right:
            if nums[left] + nums[right] < target:
                pairs += right - left
                left += 1
            else:
                right -= 1

        return pairs


sol = Solution().countPairs(nums=[-1, 1, 2, 3, 1], target=2)
print(sol)
