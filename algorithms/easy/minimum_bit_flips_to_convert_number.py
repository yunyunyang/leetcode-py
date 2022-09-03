# 2220. Minimum Bit Flips to Convert Number

class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        return bin(start ^ goal).count('1')

sol = Solution().minBitFlips(start = 10, goal = 7)
print(sol)