# 1208. Get Equal Substrings Within Budget

class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:        
        diff = []
        for i in range(len(s)):
            diff.append(abs(ord(s[i]) - ord(t[i])))

        max_len, used = 0, 0
        left, right = 0, 0
        while right < len(s):
            if used + diff[right] <= maxCost:
                used += diff[right]
                right += 1
            else:
                used -= diff[left]
                left += 1

            max_len = max(max_len, right - left)

        return max_len


sol = Solution().equalSubstring(s = "abcd", t = "acde", maxCost = 0)
print(sol)