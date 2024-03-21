# 3019. Number of Changing Keys

class Solution:
    def countKeyChanges(self, s: str) -> int:
        changes = 0
        for i in range(1, len(s)):
            if s[i].lower() != s[i-1].lower():
                changes += 1

        return changes


sol = Solution().countKeyChanges(s="mDVD")
print(sol)
