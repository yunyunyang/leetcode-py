# 2427. Number of Common Factors

class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        factor = 1
        factor += 1 if a % 2 == 0 and b % 2 == 0 else 0

        n = min(a, b)
        for i in range(3, n+1):
            factor += 1 if a % i == 0 and b % i == 0 else 0

        return factor


sol = Solution().commonFactors(a = 25, b = 30)
print(sol)