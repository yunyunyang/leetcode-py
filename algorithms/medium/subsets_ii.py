# 90. Subsets II

from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:        
        output, subset = [], []
        nums.sort()
        def backtrack(i):
            if i >= len(nums):
                output.append(subset.copy())
                return
            
            subset.append(nums[i])
            backtrack(i + 1)
            
            subset.pop()
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            backtrack(i + 1)
        
        backtrack(0)
        return output

sol = Solution().subsetsWithDup(nums = [1,2,2])
print(sol)