# 1137. N-th Tribonacci Number

class Solution:

    # Iteration
    # def tribonacci(self, n: int) -> int:
    #     mem = {0: 0, 1: 1, 2: 1}
    #     for i in range(3, n + 1):
    #         tri = mem[i-1] + mem[i-2] + mem[i-3]
    #         mem[i] = tri
    #     return mem[n]
    
    # Recursion
    def tribonacci(self, n: int) -> int:
        cache = {0: 0, 1: 1, 2: 1}
        
        def recursion(nb):
            if nb in cache:
                return cache[nb]
            else:
                cache[nb] = recursion(nb - 1) + recursion(nb - 2) + recursion(nb - 3)
            return cache[nb]
        
        recursion(n + 1)
        return cache[n]
    
sol = Solution().tribonacci(n = 4)
print(sol)