# 20. Valid Parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        map = {")": "(", "]": "[", "}": "{"}
        stack = []
        for c in s:
            if c not in map:
                stack.append(c)
                continue

            if not stack or stack[-1] != map.get(c):
                return False
            stack.pop()

        return not stack


sol = Solution().isValid(s="()")
print(sol)
