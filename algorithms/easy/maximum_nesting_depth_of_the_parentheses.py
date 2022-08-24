# 1614. Maximum Nesting Depth of the Parentheses

class Solution:
    def maxDepth(self, s: str) -> int:
        max, cur = 0, 0
        for i in list(s):
            if i == "(":
                cur += 1
            if i == ")":
                cur -= 1
            if cur >= max:
                max = cur

        return max

sol = Solution().maxDepth(s = "(1+(2*3)+((8)/4))+1")
print(sol)