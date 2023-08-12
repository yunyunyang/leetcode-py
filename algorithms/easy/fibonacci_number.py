# 509. Fibonacci Number

class Solution:
    # def fib(self, n: int) -> int:
    #     if n == 0:
    #         return 0
    #     if n == 1:
    #         return 1 
    #     return self.fib(n-1) + self.fib(n-2)
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        
        n1, n2 = 0, 1
        for i in range(1, n):
            n1, n2 = n2, n1 + n2
            
        return n2

sol = Solution().fib(n = 15)
print(f'sol={sol}')