# 2367. Number of Arithmetic Triplets

from typing import List

class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        output = 0
        size = len(nums)

        for i in range(size-2):
            for j in range(i+1, size-1):
                for k in range(j+1, size):
                    if i < j < k and nums[j] - nums[i] == diff and nums[k] - nums[j] == diff:
                        output += 1

        return output


sol = Solution().arithmeticTriplets(nums = [0,1,4,6,7,10], diff = 3)
print(sol)