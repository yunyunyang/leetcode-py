# 409. Longest Palindrome

class Solution:
    def longestPalindrome(self, s: str) -> int:
        chars = {}
        for c in s:
            chars[c] = chars.get(c, 0) + 1

        output = 0
        odd = 0
        for v in chars.values():
            if v % 2 == 0:
                output += v
            else:
                output += v - 1
                odd = 1

        return output + odd
    
sol = Solution().longestPalindrome(s = "ccc")
print(sol)