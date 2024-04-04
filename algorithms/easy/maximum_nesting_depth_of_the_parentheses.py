# 1614. Maximum Nesting Depth of the Parentheses

class Solution:
    def maxDepth(self, s: str) -> int:
        max_depth = 0
        stack = []

        for c in s:
            if c == '(':
                stack.append('(')
            if c == ')':
                stack.pop()

            max_depth = max(max_depth, len(stack))

        return max_depth


sol = Solution().maxDepth(s="(1+(2*3)+((8)/4))+1")
print(sol)
