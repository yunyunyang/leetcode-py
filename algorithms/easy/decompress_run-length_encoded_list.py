# 1313. Decompress Run-Length Encoded List

from typing import List

class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        encoded = []
        idx = 0
        while idx < len(nums):
            for i in range(nums[idx]):
                encoded.append(nums[idx+1])
            idx += 2

        return encoded

sol = Solution().decompressRLElist(nums = [1,2,3,4])
print(sol)