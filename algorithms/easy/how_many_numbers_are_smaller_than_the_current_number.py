# 1365. How Many Numbers Are Smaller Than the Current Number

from typing import List

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        output = []
        for i, ni in enumerate(nums):
            count = 0
            for j, nj in enumerate(nums):
                if i != j and ni > nj:
                    count += 1
            output.append(count)

        return output

sol = Solution().smallerNumbersThanCurrent(nums = [8,1,2,2,3])
print(sol)