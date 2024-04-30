# 22. Generate Parentheses

from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        output, stack = [], []

        def backtrack(left, right):
            if left == right == n:
                output.append("".join(stack))
                return
            
            if left < n:
                stack.append("(")
                backtrack(left + 1, right)
                stack.pop()
            if right < left:
                stack.append(")")
                backtrack(left, right + 1)
                stack.pop()

        backtrack(0, 0)
        return output
    
sol = Solution().generateParenthesis(n = 3)
print(sol)