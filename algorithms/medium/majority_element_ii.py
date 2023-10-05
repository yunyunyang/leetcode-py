# 229. Majority Element II

from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        floor = len(nums) // 3
        output = []
        table = {}

        for n in nums:
            if n not in table:
                table[n] = 1
            else:
                table[n] += 1

        for k in table.keys():
            if table[k] > floor:
                output.append(k)

        return output


sol = Solution().majorityElement(nums=[1, 2, 3])
print(sol)
