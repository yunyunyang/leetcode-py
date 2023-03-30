# 1876. Substrings of Size Three with Distinct Characters

class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        o = 0
        for i in range(len(s)-2):
            c = len(set(s[i:i+3]))
            o += 1 if c == 3 else 0
        return o
    
sol = Solution().countGoodSubstrings(s = "xyzzaz")
print(sol)