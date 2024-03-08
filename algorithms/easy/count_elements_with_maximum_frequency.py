# 3005. Count Elements With Maximum Frequency

from typing import List
from collections import Counter


class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        count = Counter(nums)
        max_freq = max(count.values())
        max_occr = list(count.values()).count(max_freq)
        return max_freq * max_occr


sol = Solution().maxFrequencyElements(nums=[1, 2, 2, 3, 1, 4])
print(sol)
