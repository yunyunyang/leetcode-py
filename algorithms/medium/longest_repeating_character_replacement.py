# 424. Longest Repeating Character Replacement

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        chars = {}
        l, longest, freq = 0, 0, 0

        for r in range(len(s)):
            chars[s[r]] = 1 + chars.get(s[r], 0)
            freq = max(freq, chars[s[r]])
            while (r - l + 1) - freq > k:
                chars[s[l]] -= 1
                l += 1

            longest = max(longest, r - l + 1)

        return longest


sol = Solution().characterReplacement(s="ABAB", k=2)
print(sol)
