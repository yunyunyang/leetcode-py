# 46. Permutations

from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        output = []

        if len(nums) == 1:
            return [nums.copy()]
        
        for i in range(len(nums)):
            n = nums.pop(0)
            perms = self.permute(nums)

            for perm in perms:
                perm.append(n)
            output.extend(perms)
            nums.append(n)

        return output
    
sol = Solution().permute(nums = [1,2,3])
print(sol)