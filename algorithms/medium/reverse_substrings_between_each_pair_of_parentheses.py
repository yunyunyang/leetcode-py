# 1190. Reverse Substrings Between Each Pair of Parentheses

class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for c in s:
            if c == ")":
                tmp = []
                p = stack.pop()
                while p != "(":
                    tmp.append(p)
                    p = stack.pop()
                stack.extend(tmp)
            else:
                stack.append(c)
                
        return "".join(stack)
    
sol = Solution().reverseParentheses(s = "(u(love)i)")
print(sol)