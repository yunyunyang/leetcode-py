# 2610. Convert an Array Into a 2D Array With Conditions

from typing import List

class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        o = [[nums[0]]]
        nums[0] = 0
        for i in range(1, len(nums)):
            for j in range(len(o)):
                if (nums[i] not in o[j]) & (nums[i] != 0):
                    o[j].append(nums[i])
                    nums[i] = 0

            if nums[i] != 0:                
                o.append([nums[i]])
                nums[i] = 0
            
        return o
    
sol = Solution().findMatrix(nums = [1,3,4,1,2,3,1])
print(sol)