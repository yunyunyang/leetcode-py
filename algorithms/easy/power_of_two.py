# 231. Power of Two

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        if n == 1:
            return True
        
        if n % 2 == 0:
            n /= 2
            return self.isPowerOfTwo(n)
        else:
            return False
    
sol = Solution().isPowerOfTwo(n = 1024)
print(sol)