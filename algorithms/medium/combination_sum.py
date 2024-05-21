# 39. Combination Sum

from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        output, com_sum = [], []

        def backtrack(i):
            if i >= len(candidates) or sum(com_sum) > target:
                return
            
            if sum(com_sum) == target:
                output.append(com_sum.copy())
                return
            
            com_sum.append(candidates[i])
            backtrack(i)

            com_sum.pop()
            backtrack(i + 1)

        backtrack(0)
        return output
    
sol = Solution().combinationSum(candidates = [2,3,6,7], target = 7)
print(sol)