# 2485. Find the Pivot Integer

class Solution:
    def pivotInteger(self, n: int) -> int:
        for i in range(1, n+1):
            sum_forward = sum_backward = 0
            sum_forward = (1 + i) * i // 2
            sum_backward = (i + n) * (n - i + 1) // 2
            if sum_forward == sum_backward:
                return i

        return -1
        

sol = Solution().pivotInteger(n = 8)
print(sol)