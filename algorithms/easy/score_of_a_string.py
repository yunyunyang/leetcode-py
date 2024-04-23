# 3110. Score of a String

class Solution:
    def scoreOfString(self, s: str) -> int:
        score = 0
        for i in range(1, len(s)):
            score += abs(ord(s[i]) - ord(s[i-1]))
        return score
    
sol = Solution().scoreOfString(s = "hello")
print(sol)