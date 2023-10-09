# 150. Evaluate Reverse Polish Notation

from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t == "+":
                stack.append(stack.pop() + stack.pop())
            elif t == "-":
                b, a = stack.pop(), stack.pop()
                stack.append(a - b)
            elif t == "*":
                stack.append(stack.pop() * stack.pop())
            elif t == "/":
                b, a = stack.pop(), stack.pop()
                stack.append(int(a / b))
            else:
                stack.append(int(t))

        return stack[0]


sol = Solution().evalRPN(tokens=["2", "1", "+", "3", "*"])
print(sol)
