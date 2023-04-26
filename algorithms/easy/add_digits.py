# 258. Add Digits

class Solution:
    def addDigits(self, num: int) -> int:
        if num < 10:
            return num
        
        while num >= 10:
            num = self.repeat(num)
        
        return num
        
    def repeat(self, n):
        o = 0
        while n > 0:
            r = n % 10
            o += r
            n //= 10
        return o
    

    
sol = Solution().addDigits(num = 38)
print(sol)