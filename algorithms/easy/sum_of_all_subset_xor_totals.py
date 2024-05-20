# 1863. Sum of All Subset XOR Totals

from typing import List

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        all_subset, subset = [], []
        def backtrack(i):
            if i >= len(nums):
                all_subset.append(subset.copy())
                return
            
            subset.append(nums[i])
            backtrack(i + 1)
            
            subset.pop()
            backtrack(i + 1)
            
        backtrack(0)
        
        output = 0
        for subset in all_subset:
            if len(subset) == 1:
                output += subset[0]
            elif len(subset) > 1:
                x = subset[0]
                for i in range(1, len(subset)):
                    x ^= subset[i]
                output += x
        
        return output
    
sol = Solution().subsetXORSum(nums = [1,3])
print(sol)