# 1920. Build Array from Permutation

from typing import List

class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        # return [nums[i] for i in nums]
        ans = []
        for i in range(len(nums)):
            ans.append(nums[nums[i]])

        return ans
        
sol = Solution().buildArray(nums = [0,2,1,5,3,4])
print (sol)