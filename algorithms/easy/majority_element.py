# 169. Majority Element

from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority, counter = 0, 0
        for i in nums:
            if counter == 0:
                majority = i
                counter = 1
            else:
                if majority == i:
                    counter += 1
                else:
                    counter -= 1

        return majority


sol = Solution().majorityElement(nums = [10,9,9,9,10])
print(sol)