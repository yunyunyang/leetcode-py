# 2656. Maximum Sum With Exactly K Elements

from typing import List

class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        m = max(nums)
        o = 0
        for i in range(m, m+k):
            o += i

        return o
    
sol = Solution().maximizeSum(nums = [1,2,3,4,5], k = 3)
print(sol)