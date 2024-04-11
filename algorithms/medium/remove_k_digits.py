# 402. Remove K Digits

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for n in num:
            while stack and stack[-1] > n and k:
                stack.pop()
                k -= 1
            stack.append(n)

        while k:
            stack.pop()
            k -= 1

        res = ''.join(stack).lstrip('0')
        return res if res else '0'


sol = Solution().removeKdigits("9", k=1)
print(sol)
