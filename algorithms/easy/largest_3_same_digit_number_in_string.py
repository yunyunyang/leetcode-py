# 2264. Largest 3-Same-Digit Number in String

class Solution:
    def largestGoodInteger(self, num: str) -> str:
        goods = []
        for n in range(9, -1, -1):
            goods.append(str(n)*3)

        for good in goods:
            if good in num:
                return good

        return ""


sol = Solution().largestGoodInteger(num="6777133339")
print(sol)
