# 128. Longest Consecutive Sequence

from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ns = set(nums)
        longest = 0

        for n in ns:
            if (n - 1) not in ns:
                length = 1
                while (n + length) in ns:
                    length += 1

                longest = max(longest, length)

        return longest


sol = Solution().longestConsecutive(nums=[0, 3, 7, 2, 5, 8, 4, 6, 0, 1])
print(sol)
