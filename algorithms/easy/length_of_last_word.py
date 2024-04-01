# 58. Length of Last Word

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.strip().split()
        return len(words[-1])


sol = Solution().lengthOfLastWord(s="   fly me   to   the moon  ")
print(sol)
