# 2697. Lexicographically Smallest Palindrome

class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        s = list(s)
        j = len(s)-1
        for i in range(len(s)):
            if s[i] != s[j]:
                if ord(s[i]) < ord(s[j]):
                    s[j] = s[i]
                else:
                    s[i] = s[j]
            j -= 1
       
        return "".join(s)
    
sol = Solution().makeSmallestPalindrome(s = "egcfe")
print(sol)