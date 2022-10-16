# 217. Contains Duplicate

from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)


sol = Solution().containsDuplicate(nums = [1,2,3,1])
print(sol)