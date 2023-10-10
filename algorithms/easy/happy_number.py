# 202. Happy Number

class Solution:
    def isHappy(self, n: int) -> bool:
        visit = set()
        while n not in visit:
            visit.add(n)
            n = self.sumOfSquares(n)
            if n == 1:
                return True

        return False

    def sumOfSquares(self, n: int) -> int:
        o = 0
        while n:
            digit = n % 10
            digit = digit ** 2
            o += digit
            n = n // 10
        return o


sol = Solution().isHappy(n=2)
print(sol)
