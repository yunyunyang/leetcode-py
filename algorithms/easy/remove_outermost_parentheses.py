# 1021. Remove Outermost Parentheses

class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        output = tmp = ''
        counter = 0
        for i in s:
            if i == '(':
                counter += 1
            elif i == ')':
                counter -= 1

            tmp += i
            if counter == 0:
                output += tmp[1:-1]
                tmp = ''

        return output
    

sol = Solution().removeOuterParentheses(s = "(()())(())")
print(sol)