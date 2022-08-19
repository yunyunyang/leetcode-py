# 1389. Create Target Array in the Given Order

from typing import List

class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        output = []
        for i, idx in enumerate(index):
            output.insert(idx, nums[i])

        return output

sol = Solution().createTargetArray(nums = [0,1,2,3,4], index = [0,1,2,2,1])
print(sol)