# 167. Two Sum II - Input Array Is Sorted

from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while l < r:
            s = numbers[l] + numbers[r]
            if s < target:
                l += 1
            if s > target:
                r -= 1
            if s == target:
                return [l+1, r+1]


sol = Solution().twoSum(numbers=[2, 7, 11, 15], target=9)
print(f"sol={sol}")
