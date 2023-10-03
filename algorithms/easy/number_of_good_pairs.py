# 1512. Number of Good Pairs

from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        if len(nums) == len(set(nums)):
            return 0

        hash_map = {}
        for k, v in enumerate(nums):
            if v not in hash_map:
                hash_map[v] = [k]
            else:
                hash_map[v].append(k)

        output = 0
        for i in hash_map.values():
            s = len(i)
            if len(i) > 1:
                o = s * (s - 1) // 2
                output += o

        return output


sol = Solution().numIdenticalPairs(nums=[1, 2, 3, 1, 1, 3])
print(sol)
