# 1929. Concatenation of Array

from typing import List

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums + nums

sol = Solution().getConcatenation(nums = [1,2,1])
print(sol)