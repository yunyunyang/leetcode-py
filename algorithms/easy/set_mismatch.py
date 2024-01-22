# 645. Set Mismatch

from typing import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        err = [0]*2
        for i in range(1, len(nums)+1):
            if nums.count(i) == 0:
                err[1] = i
            if nums.count(i) == 2:
                err[0] = i

        print([1, 2] ^ [1, 2])
        return err


sol = Solution().findErrorNums(nums=[1, 2, 2, 4])
# print(sol)
