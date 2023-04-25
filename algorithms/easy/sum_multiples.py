# 2652. Sum Multiples

class Solution:
    def sumOfMultiples(self, n: int) -> int:
        o = 0
        for i in range(1, n+1):
            if i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
                o += i

        return o
    
sol = Solution().sumOfMultiples(n = 7)
print(sol)