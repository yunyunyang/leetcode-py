# 78. Subsets

from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output, subset = [], []

        def dfs(i):
            if i >= len(nums):
                output.append(subset.copy())
                return

            subset.append(nums[i])
            dfs(i + 1)

            subset.pop()
            dfs(i + 1)

        dfs(0)
        return output


sol = Solution().subsets(nums=[1, 2, 3])
print(sol)
