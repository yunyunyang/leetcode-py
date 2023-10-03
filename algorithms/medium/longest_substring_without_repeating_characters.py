# 3. Longest Substring Without Repeating Characters

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        l, longest = 0, 0
        for r in range(len(s)):
            while s[r] in char_set:
                char_set.remove(s[l])
                l += 1
            char_set.add(s[r])
            longest = max(longest, len(char_set))

        return longest


sol = Solution().lengthOfLongestSubstring(s="abcabcbb")
print(sol)
