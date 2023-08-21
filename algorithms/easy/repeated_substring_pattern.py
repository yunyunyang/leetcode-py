# 459. Repeated Substring Pattern

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        for i in range(1, len(s)//2 + 1):
            if n % i == 0:
                ss = s[:i]
                if ss * (n//i) == s:
                    return True

        return False


sol = Solution().repeatedSubstringPattern(s="ababab")
print(sol)
