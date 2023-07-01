# 70. Climbing Stairs

class Solution:
    def climbStairs(self, n: int) -> int:
        a, b = 1, 1
        for i in range(n - 1):
            t = a
            a = a + b
            b = t
            
        return a
    
sol = Solution().climbStairs(n = 5)
print(sol)