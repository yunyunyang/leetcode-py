# 2413. Smallest Even Multiple

class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        if n % 2 == 0:
            return n
        return 2*n

    
sol = Solution().smallestEvenMultiple(n = 5)
print(sol)