# 191. Number of 1 Bits

class Solution:
    def hammingWeight(self, n: int) -> int:
        w = 0
        while n:
            w += n % 2
            n = n >> 1

        return w


sol = Solution().hammingWeight(n=100000000000000000000000000001011)
print(sol)
