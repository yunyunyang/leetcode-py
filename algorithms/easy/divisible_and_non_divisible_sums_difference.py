# 2894. Divisible and Non-divisible Sums Difference

class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        o = 0
        for i in range(n + 1):
            if i % m == 0:
                o -= i
            else:
                o += i

        return o


sol = Solution().differenceOfSums(n=10, m=3)
print(sol)
