# 2958. Length of Longest Subarray With at Most K Frequency

from typing import List
from collections import defaultdict


class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        nmap = {}
        n, left, maxlen = len(nums), 0, 1
        for right in range(n):
            nmap[nums[right]] = 1 + nmap.get(nums[right], 0)
            while nmap[nums[right]] > k:
                nmap[nums[left]] -= 1
                left += 1
            maxlen = max(maxlen, right - left + 1)
        return maxlen


sol = Solution().maxSubarrayLength(nums=[1, 4, 4, 3], k=1)
print(f'sol={sol}')
