# 1512. Number of Good Pairs

from typing import List

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        goodPairs = 0
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    goodPairs += 1

        return goodPairs

sol = Solution().numIdenticalPairs(nums = [1,2,3,1,1,3])
print(sol)